#@author: Aditya Kumar


#return the character most in a string

s=input("enter a string \t")
x=s.count(s[0]) 
b=s[0]
for i in range(1,len(s)):
     n=s.count(s[i])
     if(x<n):
         b=s[i]
         x=n

print(b)
