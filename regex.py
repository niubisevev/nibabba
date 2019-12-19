import re

# s = "Alex:1994,Sunny:1993"
# pattern=r"\w+:\d+"
# l = re.findall(pattern,s)
# print(l)
s="2019-54-22,2646-54-55"
pattren = r"\d{4}-\d{2}-\d{2}"
l = re.findall(pattren,s)
for i in l:
    a=re.sub(r"-",":",i)
    print(a)
