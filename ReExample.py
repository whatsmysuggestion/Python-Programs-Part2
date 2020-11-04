import re


a="hello hi welcome"
print(re.split(r"\s",a))
print(re.match("(h\w+)\W(h\w+)",a))
print(re.search("hi",a))


#a=re.compile("re*")
#print(a)