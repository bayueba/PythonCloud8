#coding=utf-8
"""
*
**
***
****
*****
****
***
**
*
"""
i=1
while i<=5:
    if i==5:
        print("* "*5)
        break
    j=1
    while j<=i:
        print("*"),
        j+=1
    print("")
    i+=1

