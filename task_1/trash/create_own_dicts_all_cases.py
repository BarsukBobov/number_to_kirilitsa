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

ONE_GENDERS={"М":'один',
             "Ж":'одна',
             "С":'одно'}

TWO_GENDERS={"М":'два',
            "Ж":'две',
            "С": 'два'}

with open('number_case.json', encoding='utf8') as f:
    dict_begin = json.load(f)
print(dict_begin)

numbers3_20=range(3, 21)
numbers30_100=range(30, 101, 10)
super_list=list(numbers3_20)+list(numbers30_100)

for number in super_list:
    l = []
    for case in cases:
        res = sumProp(number, "М", case)
        l.append(res)
    dict_inflect_words_by_case = dict(zip(cases, l))
    dict_begin.update({num2text(number): dict_inflect_words_by_case})

print(dict_begin)
write_json(dict_begin)