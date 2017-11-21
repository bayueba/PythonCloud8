#coding=utf-8
computer=1
p=input('剪刀（0）、石头（1）、布（2）')

if ((p==0) and (computer==2)) or \
    ((p==1) and (computer==0))or \
   (   (p==2) and computer==1):
    print("太low了你")
elif p==computer:
    print("再来")
else:
    print('ai,好惨')