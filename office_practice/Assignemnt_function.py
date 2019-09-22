# def mysum(numbers):
#     total = 0
#     for x in numbers:
#        total=total+x
#     return total
# print(mysum((8, 2, 3, 0, 7)))


# numbers = [1,2,3,4,5,1,4,5]
# Sum = sum(numbers)
# print(Sum)


##create a function to find the max number among 3 number
# def maximum(a, b, c):
#     x = [a, b, c]
#     return max(x)
# a = 10
# b = 14
# c = 12
# print(maximum(a, b, c))
#
# def max_of_two( x, y ):
#     if x > y:
#         return x
#     return y
# def max_of_three( x, y, z ):
#     return max_of_two( x, max_of_two( y, z ) )
# print(max_of_three(3, 6, -5))



##create a function to find the min number among 3 number
# def minimum(a, b, c):
#     x = [a, b, c]
#     return min(x)
# a = 10
# b = 14
# c = 12
# print(minimum(a, b, c))

##create a function to find the sqareroot of a given number.
# import math
# print(math.sqrt(4))


# def mysqrt():
#     a=int(input("enter ur number"))
#     import math
#     print(math.sqrt(a))
# mysqrt()

##area of a triangle
# def findArea(a,b,c):
#
#
#     if (a < 0 or b < 0 or c < 0 or (a+b <= c) or (a+c <=b) or (b+c <=a) ):
#         print('Not a valid trianglen')
#         return
#
#     # calculate the semi-perimeter
#     s = (a + b + c) / 2
#
#     # calculate the area
#     area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
#     print('Area of a traingle is %f' %area)
# a=3
# b=4
# c=5
# findArea(a,b,c)



##to check if a number is positive or negative
# def Number():
#     num = float(input("Enter a number: "))
#     if num > 0:
#         print("Positive number")
#     elif num == 0:
#         print("Zero")
#     else:
#         print("Negative number")
# Number()

##function to find out prime numbers

# def test_prime(n):
#     if (n==1):
#         return False
#     elif (n==2):
#         return True;
#     else:
#         for x in range(2,n):
#             if(n % x==0):
#                 return False
#         return True
# print(test_prime(37))


##function to convert celsius to farehnhite
# def C(f):
#     c = (5.0/9)*(f - 32)
#     return c
#
# def F(c):
#     f = (9.0/5)*c + 32
#     return f
#
# print (C(32))
# c = 100
# if c == C(F(c)):
#     print ('verified!')


def Cel_To_Fah():
    centi=int(input("enter your number: "))
    # return (centi*1.8)+32
    print((centi*1.8)+32)
# print(int(Cel_To_Fah()))
Cel_To_Fah()
##function to find the sum of natural number
# num = 16

# uncomment to take input from the user
#num = int(input("Enter a number: "))

# if num < 0:
#    print("Enter a positive number")
# else:
#    sum = 0
#    # use while loop to iterate un till zero
#    while(num > 0):
#        sum += num
#        num -= 1
#    print("The sum is",sum)

##to check leapyear
# year = int(input("enter a year: "))
#
# if(year%4==0 and (year%100!=0 or year%400==0)):
# 	print("leap year")
# else:
# 	print("not leap year")

##to display a multiplication table
n = int(input("Input a number: "))

# use for loop to iterate 10 times
for i in range(1,11):

    print(n,  'x', i,'=',n*i)
