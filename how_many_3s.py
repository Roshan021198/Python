"""

@author: Aditya Kumar
"""

a=int(input("enter number \t"))
count=0
while a!=0:
    x=a%10
    if(x==3):
        count+=1
    a=a//10
print("numbers of threes = "+str(count))
