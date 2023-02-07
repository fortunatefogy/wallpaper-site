# n=int(input("enter a number"))
# f=1
# for i in range (1,n+1):
#     f=f*i
#     print(f)

# n=int(input("enter a number"))
# i=1
# f=1
# while i<=n:
#     f=f*i
#     i = i + 1
#     print(f)

#
# n=int(input("enterv anumber"))
# rev=0
# while n>0:
#     rem=n%10
#     rev=rev*10+rem
#     n//=10
# print(rev)
#
# n=int(input("enter a number"))
# a=n
# arm=0
# while n>0:
#     rem=n%10
#     arm=arm+rem**3
#     n//=10
#
# if arm==a:
#     print(arm)
#
# else:
#     print("npt")
#
# c=0
# for i in range(1,101,1):
#     c=set(c+1)
#     b = sum(c)
#
#
# print(b)

# string=input("enter a string")
# if string==string[::-1]:
#     print("its a palindrome")
# else:
#     print("not a palindrome")

# num=int(input("enter a number"))
# rev=0
# while num>0:
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# print(rev)

# num=int(input("enter a number"))
# a=num
# arm=0
# while num>0:
#     rem=num%10
#     arm=arm+rem**3
#     num=num//10
# if a==arm:
#     print("it is amstrong")
# else:
#     print("it is not amstrong")
# n=int(input(" enter a number"))
# f=1
# for i in range(1,n+1):
#     f=f*i
#     print(f)
#
# first=0
# second=1
# print(first)
# print(second)
# for i in range(1,10):
#     third=first+second
#     first=second
#     second=third

a,b=0,1
c=int(input('enter a range'))
for i in range(c):
    print(a,end='')
    r=a+b
    a=b
    b=r


# a=0
# b=1
# c=int(input("enter a number"))
# for i in range(c):
#     print(a,end=" ")
#     r=a+b
#     a=b
#     b=r

# txt =[1,2,3,4,5]
# print(txt[::-1])


# s="amal"
# print(s[0].upper()+s[1:])

# s="amal"
# print(s.upper())


# s=[1,12,2,6,5,4,3]
# s.sort()
# a=max(s)
# s.remove(a)
# print(s)
# b=max(s)
# print(b)

# s=[1,7,54,8,9]
# s.sort()
# print(s)
# print(s[-2])

# a="the ghi hoo"
#
# print(a.title())

n = int(input("Enter the value of n: "))

for i in range(1, n+1):
    print(i, end = " ")