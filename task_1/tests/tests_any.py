import sys
import unittest

from main import sumProp


class TestStrToText(unittest.TestCase):

    def test_female(self):
        self.assertEqual(sumProp(2, "Ж", "И"), "две")

    def test_male(self):
        self.assertEqual(sumProp(2, "М", "И"), "два")

    def test_female2(self):
        self.assertEqual(sumProp(2, "Ж", "Т"), "двумя")

    def test_hundred(self):
        self.assertEqual(sumProp(137, "Ж", "Т"), "ста тридцатью семью")

    def test_hundred2(self):
        self.assertEqual(sumProp(112, "Ж", "Т"), "ста двенадцатью")

    def test_thousand(self):
        self.assertEqual(sumProp(1137, "Ж", "Т"), "одной тысячей ста тридцатью семью")

    def test_thousand2(self):
        self.assertEqual(sumProp(22137, "Ж", "Т"), "двадцатью двумя тысячами ста тридцатью семью")

    def test_thousand3(self):
        self.assertEqual(sumProp(12137, "Ж", "Т"), "двенадцатью тысячами ста тридцатью семью")

    def test_thousand4(self):
        self.assertEqual(sumProp(101137, "Ж", "Т"), "ста одной тысячей ста тридцатью семью")

    def test_thousand5(self):
        self.assertEqual(sumProp(101137, "Ж", "Р"), "ста одной тысячи ста тридцати семи")

    def test_thousand_man_two_case(self):
        self.assertEqual(sumProp(1232 , "М", "В"), "одну тысячу двести тридцать два")

    def test_thousand_female_two_case(self):
        self.assertEqual(sumProp(1232 , "Ж", "В"), "одну тысячу двести тридцать две")

    def test_million_1(self):
        self.assertEqual(sumProp(1231232 , "М", "В"), "один миллион двести тридцать одну тысячу двести тридцать два")

    def test_million_22(self):
        self.assertEqual(sumProp(22231232 , "М", "Р"), "двадцати двух миллионов двухсот тридцати одной тысячи двухсот тридцати двух")

    def test_million_12(self):
        self.assertEqual(sumProp(12231231 , "Ж", "Р"), "двенадцати миллионов двухсот тридцати одной тысячи двухсот тридцати одной")

    def test_million_101(self):
        self.assertEqual(sumProp(101231231  , "С", "П"), "ста одном миллионе двухстах тридцати одной тысяче двухстах тридцати одном")

    def test_billion_1(self):
        self.assertEqual(sumProp(1101231231, "М", "Т"), "одним миллиардом ста одним миллионом двумястами тридцатью одной тысячей двумястами тридцатью одним")

    def test_billion_22(self):
        self.assertEqual(sumProp(22101231231 , "М", "Т"), "двадцатью двумя миллиардами ста одним миллионом двумястами тридцатью одной тысячей двумястами тридцатью одним")

    def test_billion_12(self):
        self.assertEqual(sumProp(12101231231 , "М", "Т"), "двенадцатью миллиардами ста одним миллионом двумястами тридцатью одной тысячей двумястами тридцатью одним")

    def test_billion_101(self):
        self.assertEqual(sumProp(101101231231 , "М", "Т"), "ста одним миллиардом ста одним миллионом двумястами тридцатью одной тысячей двумястами тридцатью одним")



    def test_netral(self):
        self.assertEqual(sumProp(2222221, "С", "И"), "два миллиона двести двадцать две тысячи двести двадцать одно")

    def test_netral2(self):
        self.assertEqual(sumProp(2222212, "С", "И"), "два миллиона двести двадцать две тысячи двести двенадцать")

    def test_max_number(self):
        self.assertEqual(sumProp(999999999999, "Ж", "И"), "девятьсот девяносто девять миллиардов девятьсот девяносто девять миллионов девятьсот девяносто девять тысяч девятьсот девяносто девять")

    def test_exception(self):
        with self.assertRaises(BaseException):
            sumProp(1000000000000, "Ж", "И")

    def test_exception2(self):
        with self.assertRaises(BaseException):
            sumProp(-1, "Ж", "И")



