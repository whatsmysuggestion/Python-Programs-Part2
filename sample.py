'''a=10
a="hello"
a=10.5
print(a)'''

'''temp=0
def incremental(n):
    if (temp<len(n)):
        if (n[temp]%2==0):
            print("Even Number=",n[temp])
        else:
            print("Odd Number=",n[temp])

        return incremental(temp=temp+1)

i=[1,2,3,4,5,6,7,8,-1,-3,-9,-7,0]
print(incremental(i))'''
#n=0
#while(n<len(i)):
   # print()
   # n=n+1


class details:
    name=" "
    age=0
    def __init__(self,a,b):
        self.name=a
        self.age=b
    def showname(self):
        print(self.name)
    def showage(self):
        print(self.age)

d=details("Aravind",30)
d.showname()
d.showage()