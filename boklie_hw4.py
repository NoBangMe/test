import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.books.com.tw/web/sys_saletopb/books')
soup = BeautifulSoup(res.text,'html.parser')
divs = soup.find_all("div", class_="grid_24 main_column")

amount = 0
for index,each_div in enumerate(divs):
    span = each_div.find('span')
    if not span:
        continue
    a = span.find('a')
    if not a:
        continue
    bookName = a.text
    print(bookName)

    amount+=1
    if amount>21:
        break


#有時間也可以補充說明直接去find
for index,each_div in enumerate(divs):
    #找書名，有兩個a，書名和作者
    a_s = each_div.find_all('a')
    print('排名'+str(index+1)+': '+a_s[0].text)
    #找價格，有兩個b，打折和價格
    bs = each_div.find_all('b')
    print('價格: '+bs[-1].text+'元')
