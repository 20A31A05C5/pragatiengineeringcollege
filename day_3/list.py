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
