import json

import pymorphy2
morph = pymorphy2.MorphAnalyzer()
from num2t4ru import num2text
from main import sumProp

CONVERT_CASE={
    "Р": 'gent',
    "Д": 'datv',
    "В": 'accs',
    "Т": 'ablt',
    "П": 'loct'
}


def write_json(data, filename='number_case.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4 ,ensure_ascii= False)

cases=list(CONVERT_CASE)
dict_itog={}

ONE_GENDERS={"М":'один',
             "Ж":'одна',
             "С":'одно'}

TWO_GENDERS={"М":'два',
            "Ж":'две',
            "С": 'два'}


numbers=range(1,3)
print(list(numbers))



for number in numbers:
    if number==1:
        genders=['М', 'Ж', 'С']
    else:
        genders = ['М', 'Ж']

    for gender in genders:
        l = []
        for case in cases:
            res = sumProp(number, gender, case)
            l.append(res)
        dict_inflect_words_by_case = dict(zip(cases, l))
        if number==1:
            key=ONE_GENDERS[gender]
        else:
            key = TWO_GENDERS[gender]
        dict_itog.update({key: dict_inflect_words_by_case})

print(dict_itog)
write_json(dict_itog)