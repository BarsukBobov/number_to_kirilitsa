import sys

from loguru import logger
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
from num2t4ru import num2text
logger.remove(0)
logger.add(sys.stdout, colorize=False, format="<level>{level}:{file}:{function}:{line}: - {message}</level>", level="DEBUG")


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

type_counts=['тысяча', 'миллион', 'миллиард']

one_genders={"М":'один',
             "Ж":'одна',
             "С":'одно'}

two_genders={"М":'два',
            "Ж":'две',
            "С": 'два'}


def int_to_rus(num: int):
    res=num2text(num)
    logger.debug(res)
    return res

def need_gender(nSum: int):
    if  1<=nSum % 10<=2:
        if len(str(nSum))>1:
            if nSum % 100 not in  (11,12):
                return True
        else:
            return  True

def need_morph_thousand_mln_mlrd(normal_form, nSum):
    if normal_form=='тысяча':
        amount_thousand = int(str(nSum)[-5:-3])
    elif normal_form=='миллион':
        amount_thousand = int(str(nSum)[-8:-6])
    else:
        amount_thousand = int(str(nSum)[-11:-9])
    if 10< amount_thousand< 15:
        use_teens=True
    else:
        use_teens=False
    if str(amount_thousand)[-1] == '1' and not use_teens:
        return False
    # elif str(amount_thousand)[-1] in ('2','3','4') and not use_teens:
    return True



def morphing(parser, args):

    sclon = parser.inflect(set(args))
    if not sclon:
        logger.debug(type(args))

        sclon=parser.inflect({args[0]})
    morph_word = sclon.word
    return morph_word

def morph_one_word(word, nSum, sCase):

    # Выбор парсера без фиксации слова в падежах
    parsers = morph.parse(word)
    for parser in parsers:
        if not 'Fixd' in parser.tag:
            parser = parser
            break
    else:
        parser = parsers[0]

    # Проверка слов тысяча, млн,млрд
    if not parser.normal_form in type_counts:
        args = [convert_case[sCase]]
        return morphing(parser, args)

    if need_morph_thousand_mln_mlrd(parser.normal_form, nSum):
        args = [convert_case[sCase], 'plur']
    else:
        args = [convert_case[sCase], 'sing']
    return morphing(parser, args)


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
                some_words[-1]=one_genders[sGender]
            else:
                some_words[-1] = two_genders[sGender]
            return " ".join(some_words)
        else:
            return string

    #Если НЕ именительный падеж и род имеет значение
    if gender:
        for word in some_words[:-1]:
            morph_word=morph_one_word(word, nSum, sCase)
            end_word += str(morph_word) + ' '
        args=[convert_case[sCase], convert_gender[sGender]]
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
    res=sumProp(154323, "Ж", "И")
    logger.info(res)