import turtle
import colorsys

t=turtle.Turtle()
t.speed(0)
turtle.Screen().bgcolor('black')
t.pensize(2)
n =100
h=0

for i in range(4):
    for i in range(30):
        c = colorsys.hsv_to_rgb(h,1,0.6)
        h+=1/n
        t.color(c)
        t.circle(10+i*5,90)
        t.forward(90)
        t.left(90)
    t.right(90)
turtle.done()

"""
a=int(input("SON KIRITING : "))

if a>0 :
    a=a+1
    print("hosil bo'lgan son : ",a)
else :
    print(a)"""

#if2
"""a=int(input("a ni kiriting : "))
if a>0 :
    a=a+1
    print("a ni toping",a)
elif  a<0 :
     
    a=a-2
    print("kiriting",a)"""

#if3
"""a=int(input("a ni kiriting : "))
if a>0 :
    a=a+1
    print("a ni toping",a)
elif  a<0 :
     
    a=a-2
    print("kiriting",a)
else :
    a=10
    print(a)"""

 #if4
"""a=int(input("a ni kiriting :"))
b=int(input("b ni kiriting :"))
c=int(input("c ni kiriting :"))

if a>0 and b>0 and c>0 :
    print("hamma son musbat")

elif (a>0 and b>0 ) or (a>0 and c>0) or (b>0 and c>0) :
    print("ikkita son musbat")

elif a>0 or b>0 or c>0 :
    print("bitta son musbat")

else :
    print("hammasi 0 ga teng")"""

#if5
"""a=int(input("a ni kiriting :"))
b=int(input("b ni kiriting :"))
c=int(input("c ni kiriting :"))

if a>0 and b>0 and c>0 :
    print("hamma son musbat")

elif (a>0 and b>0 and c<0) or (a>0 and b<0 and c>0) or (a<0 and b>0 and c>0) :
    print("ikkita musbat bitta manfiy")

elif (a>0 and b<0 and c<0) or (a<0 and b>0 and c<0) or (a<0 and b<0 and c>0) :
    print("bitta musbat ikkita manfiy")

elif a<0 and b<0 and c<0 :
    print("hammasi manfiy")    

else :
    print("hammasi nolga teng")   
     """

#if6
"""a=int(input("a  ni kiriting"))
b=int(input("b ni kiriting"))
if a>b :
    print(a)
elif b>a :
    print(b)

else :
    print("ikkalasi teng")"""

#if8
"""a=int(input("a  ni kiriting"))
b=int(input("b ni kiriting"))
if a>b :
    print("eng kattasi a",a)
    print("kichkinasi b",b)
elif a<b :
    print("eng kattasi b",b)
    print("kichkinasi a",a)

else :
    print("ikkalasi teng")"""

#if9
"""a=int(input("a ni kiriting :"))
b=int(input("b ni kiriting :"))

if a>b or a==b:
    b=a+b
    print("b ni yangi qiymati :",b)
    print("a ni qiymati ",a)

elif b>a :
    print("a ni qiymati ",a)
    print("b ni qiymati katta",b)"""


#if10
"""
a=int(input("a ni kiriting"))
b=int(input("b ni kiriting"))

if a!=b :
    s=a+b
    a=a+s
    b=b+s
    print("a ni yangi qiymati",a)
    print("b ni yangi qiymati",b)

elif a==b :
    a=0
    b=0  
    print("a ni yangi qiymati",a)
    print("b ni yangi qiymati",b)  
"""









    




