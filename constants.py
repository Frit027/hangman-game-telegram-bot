from typing import Final
import emoji


TOKEN: Final[str] = "1815246769:AAGddDUoCoHRF27a2JGwFj8qmtSno5f6dSM"

COUNT_STAGES: Final[int]   = 7
STAGES: Final[tuple]       = tuple([f"resource/images/stage{i}.png" for i in range(1, COUNT_STAGES + 1)])
WORDS_FILE: Final[str]     = "resource/words.txt"

START_TEXT: Final[str]     = "Прежде чем начать играть, возможно, тебе следует ознакомиться с правилами."
RULES_TEXT: Final[str]     = "В игре 'Виселица' надо отгадывать слова. Игра состоит из 10 слов. " \
                             "Изначально в слове будет открыта одна буква.\nТебе надо отгадать " \
                             "остальные. За неверный выбор буквы на виселице будет появляться " \
                             "новая часть. Если виселица полностью нарисуется, то игра закончится." \
                             "\nУдачи!"

WIN_TEXT: Final[str]       = "Поздравляем! Слово угадано! Хотите начать новую игру?"
GAME_OVER_TEXT: Final[str] = "Упс! Вы не угадали. Загаданное слово было: %s. Хотите начать новую игру?"
GOODBYE_TEXT: Final[str]   = "Хорошо, приходи как захочешь."
SEND_LTR_TEXT: Final[str]  = "Отправь русскую букву."
WARNING_TEXT: Final[str]   = "Чтобы начать игру, нажмите на кнопку."

GO_BUTTON_TEXT: Final[str]       = f"Начинаем {emoji.emojize(':rocket:')}"
RULES_BUTTON_TEXT: Final[str]    = f"Правила {emoji.emojize(':scroll:')}"
NEW_GAME_BUTTON_TEXT: Final[str] = f"Хочу {emoji.emojize(':grinning_face_with_big_eyes:')}"
END_BUTTON_TEXT: Final[str]      = f"В другой раз {emoji.emojize(':unamused_face:')}"
