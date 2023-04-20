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
for gender in convert_gender:
    for case in convert_case:
        print(f"self.assertEqual(case('два', '{gender}', '{case}'), 'два')")
