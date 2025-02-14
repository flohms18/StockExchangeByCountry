import random as rd

Stock = {}

for i in range(2010,2020):
    Stock[i] = {
        'CAC40' : rd.randint(1,100),
        'NASDAQ' : rd.randint(1,100),

    }
    if Stock[i]['CAC40'] < Stock[i]['NASDAQ']:
        print("C WINS")
    else:
        print("N WINS")



    