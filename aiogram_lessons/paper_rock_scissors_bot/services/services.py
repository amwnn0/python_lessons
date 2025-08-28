from random import randint

from aiogram_lessons.paper_rock_scissors_bot.lexicon.lexicon import LEXICON_RU


def get_winner(user_choice):
    if user_choice == LEXICON_RU['paper']:
        answer = 1
    elif user_choice == LEXICON_RU['rock']:
        answer = 2
    else:
        answer = 3
    variant = randint(1, 3)
    if answer == variant:
        return LEXICON_RU['same_answer']
    else:
        if variant == 1:
            if answer == 2:
                return LEXICON_RU['lose']
            else:
                return LEXICON_RU['win']
        elif variant == 2:
            if answer == 1:
                return LEXICON_RU['win']
            else:
                return LEXICON_RU['lose']
        else:
            if answer == 1:
                return LEXICON_RU['lose']
            else:
                return LEXICON_RU['win']
