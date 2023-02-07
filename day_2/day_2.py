"""a,b,c=10,20,30
print(a,b,c,sep=',')
print('16','b','44',sep='-')
apple=100
banana=200
pineapple=300
print(apple,end=' ')
print(banana,end=' ')
print(pineapple)
print(apple,banana,pineapple)
x,y,z=input("Enter a three values:").split('0')
print("Total number of students:",x)
print("Number of boys is:",y)
print("Number of girls is:",z)
email="vinay@gmail.com"
pwd=12345678
cemail=input("Enter the email:")
cpwd=int(input("Enter the pwd:"))
if(email==cemail and pwd==cpwd):
    print("Login Succesful")
else:
    print("Login Failed")
    
a=5
b=5.0
if(a==b):
    print("yes")
else:
    print("no")
    
a=5
b=True
if(0==b):
    print("yes")
else:
    print("no")"""

"""x=int(input("Enter x value:"))
if(x%7==0):
    print("Divisible")
else:
    print("Not Divisible")
email="vinay@gmail.com"
pwd=12345678
otp=5678
cemail=input("Enter the email:")
cpwd=int(input("Enter the pwd:"))
if(email==cemail and pwd==cpwd):
    cotp=int(input("Enter the otp:"))
    if(otp==cotp):
        print("Order placed Succesfully")
    else:
        print("Order Failed")
elif(email!=cemail and pwd==cpwd):
    print("Login failed due to mail")
elif(email==cemail and pwd!=cpwd):
    print("Login failed due to pwd")
elif(email!=cemail and pwd!=cpwd):
    print("Login failed due to mail and pwd")
a='vinay'
print("d" in a)
for i in range(65,91):
    if i==65 or i==69 or i==73 or i==79 or i==85:
        print(chr(i),end=' ')"""

"""days=84
calls=3000
data=2.0
msg=100
a=int(input("Enter the day:"))
if a<=84:
    b=int(input("Enter the calls:"))
    c=int(input("Enter the messages:"))
    d=int(input("Enter the data:"))
    print("your plan will expire in",84-a,"days")
    print("yet to call ",3000)
else:
    print("your plan expired")
days=int(input("day:"))
if days<=84:
    calls=int(input("calls:"))
    msgs=int(input("msgs:"))
    data=float(input("data:"))
    print("reamaining days are",3000-calls) if calls<=3000 else print("kindly top up")
    print("remaining msgs are",100-msgs) if msgs<=100 else print("msg failed")
    print("remaining data is",(2.0-data)) if data<=2.0 else print("you exceeded your limit.Speed is reduced")
else:
    print("your plan expired")"""
    
for i in range(1,30):
    if(i%2==1 and i<=5):
        print (i)
        
for i in range(1,6,2):
    print (i*5)
    
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")
    
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print("\n")
    
    
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")
    
for i in range(97,123):
    for j in range(97,i+1):
        print(chr(i),end=" ")
    print("\n")
    
for i in range(97,123):
    for j in range(99,i+1):
        print(chr(i),end=" ")
    print("\n")
    
for i in range(97,123,2):
    for j in range(97,i+1):
        print(chr(i),end=" ")
    print("\n")
    
for i in range(1,11):
    print(i,"*10 =",i*10)
    
"""a=1
while(a==10):
    print(a,"* 5 =",a*5)
a+1
i=1
while i<=5:
    j=1
    while j<=i:
        print(i,end=" ")
        j=j+1
    print("\n")
    i=i-1"""


age=[10,30,-50,60,200,105,1000,305,11,22]
for i in range(len(age)):
    if age[i]%10==0:
        print(age[i])
        
l=[10,20,50,105,11]
for i in range(len(l)):
    if 0 in str(l(i)):
        print(l[i])
