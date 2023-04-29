import unittest

import pymorphy2
import num2rus
morph = pymorphy2.MorphAnalyzer()


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





def case(nSum:str, sGender: str,sCase: str):
    some_words = nSum.split()
    end_word = ''
    for word in some_words:
        parsers = morph.parse(word)
        for parser in parsers:
            if not 'Fixd' in parser.tag:
                parser=parser
                break
        else:
            parser=parsers[0]
        sclon = parser.inflect({convert_case[sCase], convert_gender[sGender]})
        if not sclon:
            sclon = parser.inflect({convert_case[sCase]})
        end_word += str(sclon.word) + ' '
    res = end_word.strip()
    return res

class TestStrToText(unittest.TestCase):

    def test_without_int_male(self):
        self.assertEqual(case('два', 'М', 'И'), 'два')
        self.assertEqual(case('два', 'М', 'Р'), 'двух')
        self.assertEqual(case('два', 'М', 'Д'), 'двум')
        self.assertEqual(case('два', 'М', 'В'), 'два')
        self.assertEqual(case('два', 'М', 'Т'), 'двумя')
        self.assertEqual(case('два', 'М', 'П'), 'двух')

    def test_without_int_female(self):
        self.assertEqual(case('два', 'Ж', 'И'), 'две')
        self.assertEqual(case('два', 'Ж', 'Р'), 'двух')
        self.assertEqual(case('два', 'Ж', 'Д'), 'двум')
        self.assertEqual(case('два', 'Ж', 'В'), 'две')
        self.assertEqual(case('два', 'Ж', 'Т'), 'двумя')
        self.assertEqual(case('два', 'Ж', 'П'), 'двух')

    def test_without_int_neutral(self):
        self.assertEqual(case('два', 'С', 'И'), 'два')
        self.assertEqual(case('два', 'С', 'Р'), 'двух')
        self.assertEqual(case('два', 'С', 'Д'), 'двум')
        self.assertEqual(case('два', 'С', 'В'), 'два')
        self.assertEqual(case('два', 'С', 'Т'), 'двумя')
        self.assertEqual(case('два', 'С', 'П'), 'двух')

    def test_without_int_male_manyWords(self):
        self.assertEqual(case('сто пятьдесят четыре тысячи триста двадцать три', "М", "Т"), "ста пятьюдесятью четырьмя тысячами тремястами двадцатью тремя")


    def test_100(self):
        self.assertEqual(case('сто', 'М', 'И'), 'сто')
        self.assertEqual(case('сто', 'М', 'Р'), 'ста')
        self.assertEqual(case('сто', 'М', 'Д'), 'ста')
        self.assertEqual(case('сто', 'М', 'В'), 'сто')
        self.assertEqual(case('сто', 'М', 'Т'), 'ста')
        self.assertEqual(case('сто', 'М', 'П'), 'ста')

    def test1(self):
        self.assertEqual(case("тридцать один", "М", "Р"), "тридцати одного")
