import requests
from urllib.request import urlretrieve
import re
import time


def geturl(url):
	try:
		requ = requests.get(url, headers={
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'})
		req = requ.text
		regexname = re.compile(r'官网：<a href="(.*?)">')
		prename = regexname.findall(req)
		f = open('list.txt','w')
		for i in prename :
			i+='\n'
			f.write(i)
		f.close()
	except:
		print("wrong")


if __name__ == '__main__':
	url = 'https://www.duyaoss.com/archives/3/'
	geturl(url)
	print("over")