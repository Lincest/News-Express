# coding=utf-8
import requests
import re
from bs4 import BeautifulSoup as bs

def geturl(url):
    try:
        requ = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'})
        requ.encoding = requ.apparent_encoding
        req = requ.text
        return req
    except:
        print("wrong")


if __name__ == '__main__':
    x = 0
    flag = 0
    cnt = 0
    retry=0
    body = []
    while(x <= 50) :
        try:
            url = 'https://jwc.xidian.edu.cn/'
            text = geturl(url)
            regex = re.compile(r'<a href="(.*?)" class="c49782"')
            body = regex.findall(text)
            print("successful")
            x=100
        except:
            x+=1
            continue

    print(body)
    with open("./update.txt", "r", encoding="utf-8") as f:
        date = f.read()
    newbody = []
    if(date == body[0]):
        flag = 1

    for i in body:
        if(date == i):
            break  # 到此为止, 之后的为之前内容
        else:
            newbody.append(i)
    date = body[0]
    body = newbody

    with open("./update.txt", "w", encoding="utf-8") as f:
        f.write(date)

    if(flag==0):
        with open("./text.html", "w", encoding="utf-8") as f:
            f.write(r"<h1>今日更新内容 :<br><br><br> </h1>")
            for i in body:
                print(i)
                if(retry < 100):
                    try:
                        tmp = i
                        url = 'https://jwc.xidian.edu.cn/' + i
                        html = geturl(url)
                        soup = bs(html, 'html.parser')
                        title = soup.find(name="td", attrs={"class" : "titlestyle49757"})
                        text = soup.find(name="div", attrs={"class" :"v_news_content"})
                        #print(str(title))
                        # print(str(text))
                        f.write(r"<h1>"+str(title)+r"</h1>"+r"&nbsp url : <a href="+url+r">" + url + r"</a>")
                        f.write(str(text))
                        f.write(r"<br><br><br><br><br><br><br>")
                        print("写入成功")
                    except:
                        i = tmp
                        print("wrong, next")
                        retry+=1  # 重复尝试
    else:
        with open("./text.html", "w", encoding="utf-8") as f:
            f.write(r"<h1>今天没有更新哦~~~</h1>")


    f.close()
    print("successful")
