import random
l=[9,3,6,8,7,5,4]
#print (l)

pivot=len(l)//2
print(pivot)

for j in range(len(l)-1):
    i=0
    while i <= len(l)-2:
        if l[i] > l [i+1]:
            x=l[i]
            l[i]=l[i+1]
            l[i+1]=x

        i += 1
print (l)