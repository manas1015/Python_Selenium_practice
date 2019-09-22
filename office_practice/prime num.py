# def test_prime(n):
#     if (n==1):
#         return False
#     elif (n==2):
#         return True;
#     else:
#         for x in range(2,n):
#             if(n % x==0):
#                 return False
#             else:
#                 return True
# print(test_prime(13))

# def findSum(n) :
#     sum = 0
#     x = 1
#     while x <=n :
#         sum = sum + x
#         x = x + 1
#     return sum
#
# n = 5
# print(findSum(n))


def primenumber():
    n=int(input("enter ur number: "))
    if n<0:
        print("it is invalid number")
    elif n==0:
        print("is is zero , not prime number")
    elif n==1:
        print("it is not prime number")
    elif n==2:
        print("it is a prime number")
    else:
        for x in range(2,n):
            if (n%x==0):
                print ("not a prim number")
                break
        else:
            print("it is  a prime num")

            # print("it is a prime number")

primenumber()


# function to find the factorial of a number
def factorial():
    num=int(input("Please enter the number: "))
    factorial=1
    if num ==0:
        print("factorial of zero is 0")
    else:
        for x in range(1,num+1):
            factorial=factorial*x

            print(factorial)

factorial()


# num = 7
#
# # uncomment to take input from the user
# #num = int(input("Enter a number: "))
#
# factorial = 1
#
# # check if the number is negative, positive or zero
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)




