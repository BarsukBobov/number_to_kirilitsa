from num_to_nom import num2text
import json


with open("number_case.json", encoding='utf8') as f:
    number_case = json.load(f)

TYPE_COUNTS = [('тысячи', 'тысяч'), ('миллиона', 'миллионов'), ('миллиарда', 'миллиардов')]
ONE_GENDERS = {"М": 'один',
               "Ж": 'одна',
               "С": 'одно'}
TWO_GENDERS = {"М": 'два',
               "Ж": 'две',
               "С": 'два'}

def morph_one_word(word, sCase):
    # Проверка слов тысяча, млн,млрд
    for i, tuples in enumerate(TYPE_COUNTS):
        if word in tuples:
            if i == 0:
                word = 'тысячи'
            if i == 1:
                word = 'миллионы'
            if i == 2:
                word = 'миллиарды'
            break
    return number_case[word][sCase]


def sumProp(nSum:int, sGender: str,sCase: str):
    if not isinstance(nSum, int) or nSum<0 or nSum>999999999999:
        raise ValueError('Аргумент nSum(число) должен быть целочисленным и в области [0,999999999999]')
    if not isinstance(sGender, str):
        raise TypeError('Аргумент sGender(род) должен быть строкой')
    if not isinstance(sCase, str):
        raise TypeError('Аргумент sCase(падеж) должен быть строкой')
    string=num2text(nSum)
    some_words = string.split()
    end_word = ''

    #проверка на склоняемость по роду
    if some_words[-1]=='один':
        some_words[-1]=ONE_GENDERS[sGender]
    elif some_words[-1]=='два':
        some_words[-1] = TWO_GENDERS[sGender]

    #Если именительный падеж
    if sCase=='И':
        return " ".join(some_words)

    #Если НЕ именительный падеж
    for word in some_words:
        morph_word=morph_one_word(word, sCase)
        end_word += str(morph_word) + ' '
    res = end_word.strip()
    return res


if __name__=="__main__":
    res=sumProp(123213, "Ж", "Т")
    print(res)