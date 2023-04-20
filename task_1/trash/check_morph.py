import pymorphy2
morph = pymorphy2.MorphAnalyzer()
word="тысячи"
for parser in morph.parse(word):
    for lexeme in parser.lexeme:
        print(lexeme)

