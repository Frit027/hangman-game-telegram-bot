from constants import STAGES, WORDS_FILE, COUNT_STAGES
import random
import re


class HangmanGame:

    def __init__(self, current_word: str = None, current_hidden_word: str = None) -> None:
        self.__current_stage_idx = 0
        self.__current_word = current_word
        self.__current_hidden_word = current_hidden_word

    @property
    def current_stage(self) -> bytes:
        with open(STAGES[self.__current_stage_idx], "rb") as f:
            self.__current_stage_idx += 1
            return f.read()

    @property
    def current_hidden_word(self) -> str:
        return ' '.join(self.__current_hidden_word)

    @property
    def current_word(self) -> str:
        return self.__current_word

    def is_true_letter(self, letter: str) -> bool:
        if letter not in self.__current_hidden_word and letter in self.__current_word:
            self.open_letter(letter)
            return True
        return letter in self.__current_hidden_word

    def open_letter(self, letter: str) -> None:
        for i, val in enumerate(self.__current_word):
            if letter == val:
                self.__current_hidden_word = self.__current_hidden_word[:i] \
                                             + letter \
                                             + self.__current_hidden_word[i + 1:]

    def is_guessed_word(self) -> bool:
        return self.__current_word == self.__current_hidden_word

    def new_level(self) -> None:
        current_word = HangmanGame.__get_game_word()
        self.__init__(current_word, HangmanGame.__get_hidden_word(current_word))

    def is_game_over(self) -> bool:
        return self.__current_stage_idx == COUNT_STAGES

    @staticmethod
    def __get_game_word() -> str:
        with open(WORDS_FILE, 'r', encoding="utf-8") as f:
            return random.choice(f.read().split('\n'))

    @staticmethod
    def __get_hidden_word(word: str) -> str:
        return re.sub(r'[^' + random.choice(word) + r']', '_', word)
