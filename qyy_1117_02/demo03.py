#coding=utf-8
# print('*')
# print("**")
# print("***")
# print("****")
i=1
while i<11:
    j=1
    while j<=i:
        print("%d*%d=%d"%(j,i,i*j)),
        j+=1
    print('')
    i+=1