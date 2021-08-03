import constants
from hangman_game import HangmanGame
from markup import reply_markup_start, reply_markup_end, reply_markup_new_game
import re
import telebot
from typing import Dict


bot = telebot.TeleBot(constants.TOKEN)
games: Dict[int, HangmanGame] = {}


@bot.message_handler(commands=['start'])
def start_command(message: telebot.types.Message) -> None:
    show_choice(message.chat.id, constants.START_TEXT, reply_markup_start)


def help_command(chat_id: int) -> None:
    show_choice(chat_id, constants.RULES_TEXT, reply_markup_new_game)


def go_command(chat_id: int) -> None:
    if chat_id not in games.keys():
        games[chat_id] = HangmanGame()
    games[chat_id].new_level()

    bot.send_message(chat_id, games[chat_id].current_hidden_word)
    bot.send_message(chat_id, constants.SEND_LTR_TEXT)


@bot.message_handler(content_types=['text'])
def reception_text(message: telebot.types.Message) -> None:
    if message.chat.id not in games.keys():
        show_choice(message.chat.id, constants.WARNING_TEXT, reply_markup_new_game)
    elif is_incorrect_input(message.text.lower()):
        bot.send_message(message.chat.id, constants.SEND_LTR_TEXT)
    else:
        send_game_message(message)


def send_game_message(message: telebot.types.Message) -> None:
    chat_id: int = message.chat.id
    if games[chat_id].is_true_letter(message.text.lower()):
        bot.send_message(chat_id, games[chat_id].current_hidden_word)
        if games[chat_id].is_guessed_word():
            show_choice(chat_id, constants.WIN_TEXT, reply_markup_end)
            del games[chat_id]
    else:
        bot.send_photo(chat_id, photo=games[chat_id].current_stage)
        bot.send_message(chat_id, games[chat_id].current_hidden_word)
        if games[chat_id].is_game_over():
            show_choice(chat_id, constants.GAME_OVER_TEXT % games[chat_id].current_word, reply_markup_end)
            del games[chat_id]


def show_choice(chat_id: int, text: str, reply_markup: telebot.types.InlineKeyboardMarkup) -> None:
    bot.send_message(chat_id,
                     text=text,
                     reply_markup=reply_markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_continue_game(call: telebot.types.CallbackQuery) -> None:
    if call.data == "yes":
        go_command(call.message.chat.id)
    elif call.data == "no":
        bot.send_message(call.message.chat.id, constants.GOODBYE_TEXT)
        start_command(call.message)
    elif call.data == "go":
        go_command(call.message.chat.id)
    elif call.data == "rules":
        help_command(call.message.chat.id)


def is_incorrect_input(input_text: str) -> bool:
    return len(input_text) > 1 or \
           re.match('[а-я]', input_text) is None
