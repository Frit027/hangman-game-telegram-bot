from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import constants


reply_markup_start = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text=constants.GO_BUTTON_TEXT,
                              callback_data="go"),
         InlineKeyboardButton(text=constants.RULES_BUTTON_TEXT,
                              callback_data="rules")
         ]
     ]
)

reply_markup_new_game = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text=constants.GO_BUTTON_TEXT,
                              callback_data="go")
         ]
     ]
)

reply_markup_end = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text=constants.NEW_GAME_BUTTON_TEXT,
                              callback_data="yes"),
         InlineKeyboardButton(text=constants.END_BUTTON_TEXT,
                              callback_data="no")
         ]
    ]
)
