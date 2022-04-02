import re
gmail=input('輸入gmail帳號')
if re.fullmatch("^\w+(@gmail.com)$",gmail)!=None:
    print('符合gmail格式')
else:
    print('不符合gmail格式')