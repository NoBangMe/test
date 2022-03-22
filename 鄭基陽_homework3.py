import requests 
from bs4 import BeautifulSoup
respond = requests.get("https://www.books.com.tw/web/sys_saletopb/books")
soup = BeautifulSoup(respond.text, "html.parser")
lis = soup.find_all("li",class_="item")


for index,each_li in enumerate(lis[:3]):    
    bookName = "" #書名每次迴圈都清空，才不會被前一次搜尋影響
    img = each_li.find("img")
    imgSrc = img['src']
    
    imgRespond = requests.get(imgSrc)
    
   
    div = each_li.find("div", class_="type02_bd-a")
    h4 = div.find('h4')
    if not h4:
        continue
    a = h4.find('a')
    if not a:
        continue
    bookName = str(index+1)+'-'+a.text

    ul = div.find('ul')
    li = ul.find('li')
    strong = li.find('a')
    if strong:
        bookName = bookName+'-'+strong.text

    with open(bookName+".jpg","bw") as file:
        file.write(imgRespond.content)
