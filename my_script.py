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
    print("start working.. ")
    while(x <= 50) :
        try:
            url = 'https://jwc.xidian.edu.cn/tzgg.htm'
            text = geturl(url)
            soup = bs(text,'html.parser')
            html = soup.find(name="div",attrs={"class":"list"})
            bodybf = html.find_all('a')
            for k in bodybf:
                if(k['href'] and k['href'].find("info") != -1):
                    body.append(k['href'])
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
            break  # 到此为止, 之后的为之前已经更新内容
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
                retry = 0
                while(retry < 100):               
                    try:
                        url = 'https://jwc.xidian.edu.cn/' + i
                        html = geturl(url)
                        soup = bs(html, 'html.parser')
                        title = soup.find(name="p", attrs={"class" : "tit"})
                        text = soup.find(name="div", attrs={"class" :"v_news_content"})
                        #print(str(title))
                        # print(str(text))
                        f.write(r"<h1>"+str(title)+r"</h1>"+r"&nbsp url : <a href="+url+r">" + url + r"</a>")
                        f.write(str(text))
                        f.write(r"<br><br><br><br><br><br><br>")
                        retry = 1000
                    except:
                        retry+=1  # 重复尝试
        with open("./update","w",encoding="utf-8") as f : 
            f.write("true")

    else:
        with open("./text.html", "w", encoding="utf-8") as f:
            f.write(r"<h1>今天没有更新哦~~~</h1>")
        with open("./update","w",encoding="utf-8") as f : 
            f.write("false")

    with open("./runtimes.txt", "r", encoding="utf-8") as f:
        x = f.read()

    x = str(int(x) + 1)
    with open("./runtimes.txt", "w", encoding="utf-8") as f:
        f.write(x)


    f.close()
    print("successful")
