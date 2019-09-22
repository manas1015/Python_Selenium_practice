# def myfunction():
#     # num=23
#     num=int(input("enter your number"))
#     if num%2 ==0:
#         print("even")
#     else:
#         print("odd")
#
# # print("end of myfunction")
# myfunction()


# def myfunction(inputNumber):
#
#     num=inputNumber
#     if num%2 ==0:
#         print("even")
#     else:
#         print("odd")
#
# myfunction(20)
# myfunction(45)
# myfunction(50)


# def addTwoNumber(num1 , num2):
#     sum=num1+num2
#     print(sum)

# def modifiedAdd(num1 , num2):
#     sum=num1+num2
#     return sum
#
# print(modifiedAdd(12 ,44))
#
# sumVariable =modifiedAdd(12,56)
#
# print(sumVariable - 100)
# # sub=sum -55
# print(sub)

#add list of number

# def ListAdd():
#     List = [10, 20, 30, 40]
#     sum=0
#     for x in List:
#         sum=sum+x
#         print(sum)
# LirstAdd()

def Num():
    Num = int(input("enter number: "))
    if Num <0:

         print("negative")
         return Num()

    elif Num==0:
        print("zero")
    else:
        return("positive")

Num()

# if Num = '-':
#     print("this is a negative number")
# else:
#     print("this is a positive number ")
