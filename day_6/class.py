#program to create  and access an object
class abc:
    attribute=10
obj=abc()
print(obj.attribute)

#program to create self arg  and access an object
class abc:#2
    attribute=10#3
    def display(self):#6
        print('this is in class')#7        
obj=abc()#1
print(obj.attribute)#4
obj.display()#5'''

# constructor
class abc:
    def __init__(self,value):
        print('this is in class')
        self.value=value
        print('the value is ',value)
obj=abc(100)
