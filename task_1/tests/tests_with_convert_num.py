import sys
import unittest

from main import sumProp



class TestStrToText(unittest.TestCase):

    def test1(self):
        self.assertEqual(sumProp(31, "М", "Р"), "тридцати одного")

    def test2(self):
        self.assertEqual(sumProp(22, "С", "Т"), "двадцатью двумя")

    def test3(self):
        self.assertEqual(sumProp(154323, "М", "И"), "сто пятьдесят четыре тысячи триста двадцать три")

    def test4(self):
        self.assertEqual(sumProp(154323, "М", "Т"), "ста пятьюдесятью четырьмя тысячами тремястами двадцатью тремя")


