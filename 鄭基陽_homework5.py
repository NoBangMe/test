import requests

respond=requests.get("https://www.dcard.tw/service/api/v2/forvms/pet/posts?popular=true&limit=40")
jsonData=respond.json()

for data in jsonData:
    count=1
    title=data['title']
    for picture in data['media']:
        try:
            with open("asdwasd/images/"+title+str(count)+".jpg","bw")as file:
                file.write(requests.get(picture['url']).content)
                print("成功download"+titel+str(count)+".jpg")
            except Exception as e:
                print(e)
                
            count+=1
