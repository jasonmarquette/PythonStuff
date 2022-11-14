#!/usr/bin/python3
import re


name = "jason"
print("Hello world!")

print("Hello", name)

f= open("test.txt", "r")
for x in f:
    s=x
    s = re.search("last",x)

    if s:
        print("Match")
    else:
        print("no match")
    print(x)
# print (f.read())



