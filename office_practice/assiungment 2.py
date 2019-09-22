#########filling an array with random numbers in python

# import random
# x = random.random()
# print(x)

# import random
#
# mylist = []
#
# for i in range(0,100):
#     i = random.randint(1,100)
#     mylist.append(i)
#
# print(mylist)



#######find out how may odd and even numbers in the list using python
# list1 = [10, 21, 4, 45, 66, 93, 1,100]
# even_count= 0
# odd_count= 0
# for num in list1:
#     if num % 2 == 0:
#         print()
#         even_count =even_count+1
#     else:
#         odd_count += 1
# print("Even numbers in the list: ", even_count)
# print("Odd numbers in the list: ", odd_count)

# even_number=[]
# odd_number=[]
# num=int(input("enter your range:"))
# for x in range(0,num):
#     if x%2==0:
#         even_number.append(x)
#     else:
#         odd_number.append(x)
# print("Even number:",even_number)
# print("odd Numbers:" ,odd_number)


#######separate positive numbers form negative using python

# list1 = [10, -21, 4, -45, 66, -93, 1]
# pos_count =neg_count = 0
# for num in list1:
#     if num >= 0:
#         pos_count += 1
#
#     else:
#         neg_count += 1
#
# print("Positive numbers in the list: ", pos_count)
# print("Negative numbers in the list: ", neg_count)


# list1 = [10, -21, 4, -45, 66, -93, 1]
# for num in list1:
#     if num>0:
#         print("positive")
#     else:
#         print("negative")


# A = [1, -3, -2, 8, 4, -5, 6, -7]
# B = []
# C = []
# for x in A:
#     if (x >= 0):
#         B.append(x)
#
#
#     else:
#         C.append(x)
# print(B)
# print(C)


#####find the longest word in the string
def find_longest_word():
    longest_word = ''
    length=0
    word_list="I am form odisha"
    for word in word_list.split():
        if len(word) > len(longest_word):
            longest_word = word
            length=len(word)


    print (longest_word)
    print(length)
find_longest_word()


###########separate 0 and 1 from the list and make two sublists in python
# ini_list = [[1, 2], [4, 3], [45, 65], [223, 2]]
# print ("initial list", str(ini_list))
# res1 = [i[1] for i in ini_list]
# res2 = [i[0] for i in ini_list]
# print("final lists", str(res1), "\n", str(res2))

########create a dictionary from two lists in python
# test_keys = ["Rash", "Kil", "Varsha"]
# test_values = [1, 4, 5]
# print ("Original key list is : " + str(test_keys))
# print ("Original value list is : " + str(test_values))
# res = dict(zip(test_keys, test_values))
# print ("Resultant dictionary is : " +  str(res))
#


##########create a function for fabonaccie series
# def Fab():
#     num=int(input("Enter ur number:"))
#     n1=1
#     n2=1
#     sum=0
#     for x in range(0,num):
#         sum=n1 + n2
#         n1=n2
#         n2=sum
#         print(sum)
# Fab()

####substring
# str1="I am from odisha odisha"
# str2="odisha"
# print(str1.count("odisha"))

