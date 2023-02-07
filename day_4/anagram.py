import string
str1="silent"
str2='listen'
n=len(str1)
m=len(str2)
sortstr1=sorted(str1)
sortstr2=sorted(str2)
if n==m:
    if sortstr1==sortstr2:
        print("anagram")
    else:
        print("not an anagram")
else:
    print("not equal")
    
    
from collections import Counter
def check(str1,str2):
    if(Counter(str1)==Counter(str2)):
        print('true')
    else:
        ('false')
str1='listen'
str2='silent'
check(str1,str2)
