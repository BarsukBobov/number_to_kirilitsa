import sys

from loguru import logger
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
from num2t4ru import num2text
logger.remove(0)
logger.add(sys.stdout, colorize=True, format="<level>{level}:{file}:{function}:{line}: - {message}</level>", level="DEBUG")


convert_case={
    "И": 'nomn',
    "Р": 'gent',
    "Д": 'datv',
    "В": 'accs',
    "Т": 'ablt',
    "П": 'loct'
}
convert_gender={
    "М": 'masc',
    "Ж": 'femn',
    "С": 'neut',
}


def int_to_rus(num: int):
    res=num2text(num)
    logger.debug(res)
    return res

def sumProp(nSum:int, sGender: str,sCase: str):
    if not isinstance(nSum, int) or nSum>999999999999:
        raise ('Аргумент nSum(число) должен быть целочисленным')
    if not isinstance(sGender, str):
        raise ('Аргумент sGender(род) должен быть строкой')
    if not isinstance(sCase, str):
        raise ('Аргумент sCase(падеж) должен быть строкой')
    string=int_to_rus(nSum)
    some_words = string.split()
    end_word = ''
    for word in some_words:
        logger.debug(word)
        parsers = morph.parse(word)
        for parser in parsers:
            if not 'Fixd' in parser.tag:
                parser=parser
                break
        else:
            parser=parsers[0]

        for tag in morph.tag(word):
            if 'nomn' in tag and tag.number=='plur':
                number=tag.number
                args={convert_case[sCase], convert_gender[sGender], number}
                break
        else:
            number=None
            args={convert_case[sCase], convert_gender[sGender]}

        sclon = parser.inflect(args)
        if not sclon:
            if number:
                args = {convert_case[sCase], number}
                sclon = parser.inflect(args)
                if not sclon:
                    args = {convert_case[sCase]}
            else:
                args = {convert_case[sCase]}
            sclon = parser.inflect(args)
        end_word += str(sclon.word) + ' '
    res = end_word.strip()
    logger.debug(res)
    return res

if __name__=="__main__":
    # sumProp(999999999999, "М", "И")
    sumProp(999999999999, "М", "И")