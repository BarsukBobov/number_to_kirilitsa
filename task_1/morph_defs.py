from num2t4ru import num2text
from loguru import logger
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
CONVERT_CASE={
    "И": 'nomn',
    "Р": 'gent',
    "Д": 'datv',
    "В": 'accs',
    "Т": 'ablt',
    "П": 'loct'
}
CONVERT_GENDER={
    "М": 'masc',
    "Ж": 'femn',
    "С": 'neut',
}

TYPE_COUNTS=['тысяча', 'миллион', 'миллиард']

ONE_GENDERS={"М":'один',
             "Ж":'одна',
             "С":'одно'}

TWO_GENDERS={"М":'два',
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
    return True



def morphing(parser, args):

    sclon = parser.inflect(set(args))
    if not sclon:
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
    if not parser.normal_form in TYPE_COUNTS:
        args = [CONVERT_CASE[sCase]]
        return morphing(parser, args)

    if need_morph_thousand_mln_mlrd(parser.normal_form, nSum):
        args = [CONVERT_CASE[sCase], 'plur']
    else:
        args = [CONVERT_CASE[sCase], 'sing']
    return morphing(parser, args)
