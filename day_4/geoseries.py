#0,0,6,7,14,12,21,
term=int(input("enter the term:"))
if term%2==0:
    term=term//2
    print(6*(term-1))
else:
    term=term//2+1
    print(7*(term-1))
