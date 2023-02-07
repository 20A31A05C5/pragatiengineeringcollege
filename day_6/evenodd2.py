class number:
    even=[]
    odd=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            number.even.append(num)
        else:
             number.odd.append(num)
n1=number(11)
n2=number(12)
n3=number(13)
n4=number(14)
n5=number(15)
print('even number list is',number.even)
print('odd number list is',number.odd)
