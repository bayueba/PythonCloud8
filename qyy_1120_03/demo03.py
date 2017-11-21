#coding=utf-8
a=['qq ','bb','zz','ff']
for i in a:
    if i=='zz':
        continue
    print(i)
else:
    print("小圆是美女")

name='abcdefqwu'
print(name[0:-1:2])
print(name[0:6])
print("**"*20)
print(name[5:1:2])
print("aaa")
a="12345"
print(a[len(a)-1])
print(a.find('4',4))
print(dir(str))