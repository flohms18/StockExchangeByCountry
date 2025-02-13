import random as rd
Stock = {}

for i in range(2010,2020):
    Stock[i] = {
        'CAC40' : rd.randint(1,9),
        'NASDAQ' : rd.randint(1,9),
        'EURONEXT' : rd.randint(1,9)
    }

    print(Stock[i]['CAC40'])
    print(Stock[i]['NASDAQ'])


    if Stock[i]['CAC40'] > Stock[i]['NASDAQ']:
        print("C")
    else:
        print("W")

    