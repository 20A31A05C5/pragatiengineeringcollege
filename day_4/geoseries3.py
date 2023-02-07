#0,0,2,1,4,2,6,3,8,4
term=int(input("enter the term:"))
if term%2==0:
    term=term//2
    print(term-1)
else:
    term=term//2
    print(2*term)
    
n=int(input('enter the number:'))
a=b=0
for i in range(1,n+1):
    if(i%2!=0):
        a=a+2
    else:
        b=b+1
if(n%2!=0):
    print('{}'.format(a-2))
else:
        print('{}'.format(b-1))
