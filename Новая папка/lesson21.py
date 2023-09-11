
#a=int(input("a ni kiriting :"))
#P=a*4
#print("perimetr javobi ",P)
#a=int(input("a ni kiriting :"))
#S=a**2
#print("perimetr javobi",S)

#begin2 
"""
a=int(input("a ni kiriting:"))
b=int(input("b ni kiritinig"))
S=a*b
P=2*(a+b)
print("perimetr javobi",S)
print("perimetr javobi",P)"""

#begin4

"""a=int(input("a ni kirit:"))
b=int(input("a ni kirit:"))
c=int(input('c ni kirit:'))
V=a*b*c
S=2*(a*b+b*c+a*c)
print("найти объем",V)
print("плщшад происходинийф",S)"""

#for1
"""K=int(input('K ni kiriting : '))
N = int(input('N ni kiriting :'))

for i in range(N) :
    print(K)"""

#for2
"""
A=int(input("A ni kiritng : "))
B = int(input("B ni kiriting :"))

N = 0

for i in range(A,B+1):
    print(i)
    N+=1
print("ular soni : ",N)
"""
#for3
"""
A=int(input("A ni kiritng : "))
B = int(input("B ni kiriting :"))

N = 0

for i in range(B-1,A,-1):
    print(i)
    N+=1
print("ular soni : ",N)
"""

#for4
"""
N=int(input("narxini  kiritng : "))


for i in range(1,11):
    print(i*0.1,'kg','narxi : ',int(i*N*0.1))
"""
"""

A=int(input("A ni kiritng : "))
B = int(input("B ni kiriting :"))

N = 0

for i in range(A,B+1):
    N=N+i
print("Summasi : ",N)
"""


"""rows = 3
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")


for i in range(rows,-1,-1):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")
""""""
class Teacher:
    def __init__(self):
        self.name = input('Введите имя: ')
        self.cours = input('Введите названия курсов, через запятую: ').split(',')
 
    def python_guru(self):
        result = False
        for c in self.cours:
            if c =='Python Pro'  or c =='Python Start':
                result = True
        return result
 
new_list = []
n=int(input('n = '))
lst = [Teacher() for i in range(n)]
for obj in lst:
    if obj.python_guru():
        new_list.append(obj.name)


print("Эксперты Python:",'\n')
for i in new_list:
    print(i,'\n')"""

"""from time import *

start_time =time()
phrase = input('Напишите отзыв о нас :')
end_time = time()

total_time= end_time - start_time
symbols = len(phrase)

print('Скорость печати : ',symbols/total_time*60)"""

#for11

"""N=int(input("N sonni kiriting : "))
p=1
for i in range(11,N):
    p =p*i*0.1

print("ko'paytmasi : ",p)"""
#for8
"""A=int(input('A berilgan :'))
B=int(input('B berilgan :'))

p=1

for i in range(A,B+1):
    p=p*i

print("ko'paytmasi",p)"""


"""N=int(input("N sonni kiriting : "))
s=0
for i in range(11,N):
    s =s+i*(-0.1)
    s=s*(-1)

print("ko'paytmasi : ",s)"""

# N=int(input('N berilgan :'))

# s=0 
# for i in range(1,N+1,2):
#     s= s+i
    
# a=[1,5.5,"Salom",234,"Hi","Jumagul","Nayzangul"]

# i=0

# while(i<5):
#     print("i ni qiyamati= ",i,"  Massiv elementi =",a[i])
   
#     i=i+1
    
# K= int(input("K Sonni kirit : "))

# N= int(input("N Sonni kirit : "))

# for i in range(N):
#     print(K)

A=int(input("A sonni kirit :"))
B=int(input("B sonni kirit :"))

C=A
A=B
B=C
print("Sonlar almashdi A :",A)

print("Sonlar almashdi B :",B)
