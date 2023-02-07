def findtotalcurtains(n,number):
    total=0
    for i in numbers:
        total+=i//12
    return total
n=int(input('size='))
numbers=list(map(int,input().split()))
print(findtotalcurtains(n,numbers))
