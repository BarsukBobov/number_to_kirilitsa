import sys
import time

from loguru import logger

from morph_defs import *
logger.remove(0)
# # production
# logger.add("number_to_kirilitsa.log", colorize=False, format="<blue>{level}:{file}:{function}:{line}: - {message}</blue>", level="DEBUG",
#            rotation="1h", retention=0)
# debug
logger.add(sys.stdout, colorize=True, format="<blue>{level}:{file}:{function}:{line}: - {message}</blue>", level="INFO")


def sumProp(nSum:int, sGender: str,sCase: str):
    if not isinstance(nSum, int) or nSum<0 or nSum>999999999999:
        raise ('Аргумент nSum(число) должен быть целочисленным и в области [0,999999999999]')
    if not isinstance(sGender, str):
        raise ('Аргумент sGender(род) должен быть строкой')
    if not isinstance(sCase, str):
        raise ('Аргумент sCase(падеж) должен быть строкой')
    string=int_to_rus(nSum)
    some_words = string.split()
    end_word = ''

    #проверка на склоняемость по роду
    gender = False
    if need_gender(nSum):
        gender=True
        amount = len(some_words)

    #Если именительный падеж
    if sCase=='И':
        if gender:
            if str(nSum)[-1]=='1':
                some_words[-1]=ONE_GENDERS[sGender]
            else:
                some_words[-1] = TWO_GENDERS[sGender]
            return " ".join(some_words)
        else:
            return string

    #Если НЕ именительный падеж и род имеет значение
    if gender:
        for word in some_words[:-1]:
            morph_word=morph_one_word(word, nSum, sCase)
            end_word += str(morph_word) + ' '
        args=[CONVERT_CASE[sCase], CONVERT_GENDER[sGender]]
        morph_last_word=morphing(morph.parse(some_words[-1])[0], args)
        end_word +=morph_last_word
        res = end_word.strip()
        return res

    #Если НЕ именительный падеж и род не имеет значение
    for word in some_words:
        morph_word=morph_one_word(word, nSum, sCase)
        end_word += str(morph_word) + ' '
    res = end_word.strip()
    return res


if __name__=="__main__":
    res=sumProp(123212, "Ж", "И")
    print(res)