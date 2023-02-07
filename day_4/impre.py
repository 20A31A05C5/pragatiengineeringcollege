#match in re
import re
str1='she sells sea shells at sea shore'
p1='sells'
if re.match(p1,str1):
    print('match found')
else:
    print(p1,' not present in string')

#search in re
import re
str1='she sells sea shells at sea shore'
p1='sells'
if re.search(p1,str1):
    print('match found')
else:
    print(p1,' not present in string')
    
#replace in re
import re
str1='she sells sea shells at sea shore'
p1='sea'
rep='ocean'
ns=re.sub(p1,rep,str1,1)
print(ns)

import re
p="[aeiou]"
hh=input("enter the name:")
if re.search(p,hh):
    print("matchy vowel")
else:
    print("there is no vowel")
