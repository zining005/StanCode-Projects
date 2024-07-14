"""
File: webcrawler.py
Name: Zining Chen
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #

        # send get
        tr = soup.find_all('tr')
        boy_total = 0
        girl_total = 0
        for line in tr:
            boy_and_girl = line
            # string's data type is string. A string = Rank + Boy name + Boy amount + Girl name + Girl Amount
            string = boy_and_girl.text
            #  .split() make the data type = list
            list_ = string.split()
            # To make sure the rest of the lists which are not [ Rank, Boy name, Boy amount, Girl name, Girl Amount]
            # won't be included.
            if len(list_) == 5:
                boy_ans = ''
                boy_amount = list_[2]
                girl_ans = ''
                girl_amount = list_[4]
                for i in boy_amount:
                    # Since the amount contains ',' e.g. 16,639, we need to clean the data into digit only.
                    if i.isdigit():
                        boy_ans = boy_ans + i
                for i in girl_amount:
                    if i.isdigit():
                        girl_ans = girl_ans + i
                # To make sure there's no empty string
                if boy_ans:
                    int_boy_amount = int(boy_ans)
                    boy_total += int_boy_amount
                if girl_ans:
                    int_girl_amount = int(girl_ans)
                    girl_total += int_girl_amount
        print('Male Number: ' + str(boy_total))
        print('Female Number: ' + str(girl_total))


if __name__ == '__main__':
    main()
