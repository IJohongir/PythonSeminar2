# def make_list(number):
#     make_list.names = [input("name") for _ in range(number)]
#     print(make_list.names)
    
# number = int(input("How much"))
# make_list(number)
# for name in make_list.names:
#     if name[0] =="А":
#         print("f", name, "g")
# a=list(map(int,input("sonlarni kiriting :").split()))
# b=[]
# i=0

# while i <len(a):
#     if a[i]==2 or a[i]==3 :
#         b.append(a[i])
#         a[i]=0

#     else :
#         i=i+1

# print(a)
# print(b)


# if a<0 :
#     b1=(-1)*b
#     c1=c*(-1)
#     if b1==a :
#         print("a и b  взаимно протива положны а=",a,'b=',b)
#     elif c1==a :
#         print("a и c  взаимно протива положны а=",a,'c=',c)
#     else :
#         if b1==c :
#             print("c и b  взаимно протива положны c=",c,'b=',b)
#         else :
#             print("не совпадаймых  ")

# elif b<0 :
#     a1=(-1)*a
#     c1=c*(-1)
#     if a1==b :
#         print("a и b  взаимно протива положны а=",a,'b=',b)
#     elif c1==b :
#         print("b и c  взаимно протива положны b=",b,'c=',c)
#     else :
#         if a1==c :
#             print("a и c  взаимно протива положны c=",c,'a=',a)
#         else :
#             print("не совпадаймых  ")
# elif c<0 :
#     b1=(-1)*b
#     a1=a*(-1)
#     if b1==c :
#         print("c и b  взаимно протива положны c=",c,'b=',b)
#     elif a1==c :
#         print("a и c  взаимно протива положны а=",a,'c=',c)
#     else :
#         if b1==a :
#             print("a и b  взаимно протива положны a=",a,'b=',b)
#         else :
#             print("не совпадаймых  ")
# else :
#     print("не совпадаймых  ")

#boolean29
# N=int(input("Введите число  N"))
# K=int(input("Число K"))
# i=0
# while i<N :
#     print(K)
#     i+=1
# for a in range(N) :
    # print(K)


# a=int(input("a o'zgaruvchini kiriting : "))
# b=int(input("b o'zgaruvchini kiriting : "))
# c=int(input("c o'zgaruvchini kiriting : "))
# d=int(input("d o'zgaruvchini kiriting : "))
# g=int(input("g o'zgaruvchini kiriting : "))
# f=int(input("f o'zgaruvchini kiriting : "))


# max=0


# if a > max :
#     max = a

# if b > max :
#     max = b

# if c > max :
#     max=c

# if d > max :
#     max = d

# if g > max :
#     max = g

# if f > max :
#     max = f

# print("Sizning maximumingiz : ",max)
# import random
# n=[]
# N=int(input("Massiv hajmini kiriting : "))
# for i in range(N):
#     a = random.randint(10,100)
#     n.append(a)
# print(n)
# max=0
# min=n[0]
# for i in range(len(n)):
#     if n[i]>max:
#         max=n[i]
#     if n[i] < min :
#         min=n[i]
# print(min)
# print(max)
# S=0
# for i in range(len(n)):
#     S+=n[i]
# S_1=S-(max+min)
# print(S_1)


# count=0
# n =int(input("Enter a number "))
# array=[]
# for i in range(1,n+1):
#     cn=i
#     count=0
#     for j in range(1,cn+1):
#         if cn%j==0:
#             count+=1
#     if count==2:
#         array.append(cn)


# print(array)
# a = input('son kiriting ')

# sum=0
# multiplay=1
# for b in a:
#     sum +=int(b)
#     multiplay *=int(b)
# print(sum)
# print(multiplay)
# if sum ==multiplay:
#     print(f"{a} josus son")
# else:
#     print(f"{a} josus son emas")


# a = int(input('son kiriting '))
# lens = len(str(a))
# pops = lens-1
# b=a
# sum = 0
# for i in range(1, lens+1):
#     sum += (a//(10**pops))**i
#     a = a - ((a//(10**pops)) * (10**pops))
#     pops -= 1
# if sum == b:
#     print(f'{b} Disarium soni')
# else:
#     print(f'{b} Disarium son emas')


# sum=0

# num= int(input("Введите число : "))
# digit_count=0

# temp=num
# while temp!=0:
#     temp=temp//10
#     digit_count+=1

# temp=num
# while temp!=0:
#     pd=temp%10
#     sum = sum + pow(pd,digit_count)
#     temp=temp//10
#     digit_count -=1

# if sum == num:
#     print(num,"это число Disarium число ")

# else :
#     print(num,"это число  НЕ Disarium  ")



from random import randint

number = int(input('введите количество монет: '))

m = 0
k = 0
coins = []
for i in range(number):
    a=randint(0,1)
    coins.append(a)

for i in coins:
    if i == 0:
        k += 1
    if i == 1:
        m += 1

print(f'всего монет {m, k}')
print(coins)
if m > k:
    ans = k
else:
    ans = m

print(f"минимальное количество монет, которые нужно перевернуть  : {ans}")