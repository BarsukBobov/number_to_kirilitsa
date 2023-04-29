import pymorphy2
morph = pymorphy2.MorphAnalyzer()
word="одна"
parser=morph.parse(word)[0]
res=parser.inflect({"gent"}).word
print(res)

ewr