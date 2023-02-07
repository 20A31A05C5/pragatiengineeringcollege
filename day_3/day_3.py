a=64
b=46
print("before swapping")
print("a=",a)
print("b=",b)
a=a+b
b=a-b
a=a-b
print("after swapping")
print("a=",a)
print("b=",b)

a=64
b=46
print("before swapping")
print("a=",a)
print("b=",b)
a=a*b
b=a/b
a=a/b
print("after swapping")
print("a=",a)
print("b=",b)


a=64
b=46
print("before swapping")
print("a=",a)
print("b=",b)
a=a^b
b=a^b
a=a^b
print("after swapping")
print("a=",a)
print("b=",b)


l=[1,2,3,4,5,6,7,8,9,10]
print(l)
print("first element in list",l[1])
print(l[2:5])#slice
print(l[::2])
print(l[1::3])
print(l[::2])
del l[2:4]
print (l)
print(sum(l))

l=[1,'a',"abc",[2,3,4],5.6]
print(l[3][0])
print(len(l))

l=[4,8,-5,8,2,99,23]
print(min(l))
print(max(l))

n=int(input("enter n value:"))
i=1
s=0
while i<=n:
    s=s+i
    i+=1
print(s)

num=[6,3,7,0,1,2,4,9]
num.remove(0)
print(num)

num=[6,3,7,0,1,2,4,9]
num.reverse()
print(num)

l=[]
for i in range(0,11):
    l.append(i**3)
print(l)

print([i**3 for i in range(11)])

num=[int(d) for d in str(input("enter the number:"))]
even,odd=0,0
for i in range(0,len(num)):
    if i%2==0:
        even=even+num[i]
    else:
        odd=odd+num[i]
print(abs(odd-even))


term=int(input("enter the term:"))
if term%2==0:
    term=term//2
    print(3**(term-1))
else:
    term=term//2+1
    print(2**(term-1))
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
