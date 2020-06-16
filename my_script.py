import sys
import os

with open('./123.txt', 'r') as f:
    text = f.read()


with open('./123.txt', 'w') as f:
	if(text=="hello world\n"):
		f.write("not new")
	else :
		f.write("I'm new")

