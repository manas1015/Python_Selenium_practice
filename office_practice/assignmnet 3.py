#####Create a function to separate numbers from given integers
# txt='12345 manas 12 54 dash'
# for x in txt.split():
#      if x.isdigit():
#       print(x)


# print(y)
#####Create a func to determine the percentage of lower case and upper case letters in a given string
# def count_by_case(string):
#      upper = sum(letter.isupper() for letter in string)
#      lower = sum(letter.islower() for letter in string)
#      return lower, upper
#
# string = "MyString"
# lower, upper = count_by_case(string)
# print("{} contains {} upper and {} lower case letters".format(string, upper, lower))

#####create a function to find out of whether given string is palindrome or not
# my_str = ['aibohphobia' , 'abc']
# rev_str=my_str.reverse()
# # my_str = my_str.casefold()
# # rev_str =my_str.
# if my_str == rev_str:
#    print("It is palindrome")
# else:
#    print("It is not palindrome")
#
# x = "mannam"
# w = ""
# for i in x:
#     w = i + w
#     if (x==w):
#         print("YES")
#     else:
#         print("No")
#
# string_to_check = input("Enter a string")
#
# if string_to_check == string_to_check[::-1]:
#     print("This is a palindrome")
# else:
#     print("This is not a palindrome")


###Reverse the given string
# str1='manas'
# rev1=str1[::-1]
# print(rev1)

#####remove duplicate from the given list
# list1=[1,1,2,2,3,5,6,7,8,7]
# list2=[]
#
# for x in list1:
#     if  x not  in list2:
#
#         list2.append(x)
# print(list2)


######Check if a Substring is Present in a Given String
# str1='I am Manas'
# substr1='Manas'
# # for word in str1:
# if substr1 in str1:
#     print("The substring is : ", substr1)

#####swap commas and dots from the given string

# str1='12,54.89'
# str1=str1.replace(',','x')
# str1=str1.replace('.',',')
# str1=str1.replace('x', '.')
# print(str1)

# l=input("enter the input:")
# m=[]
# for i in l:
#  if(i=='.'):
#   m.append(',')
#  elif(i==','):
#   m.append('.')
#  else:
#   m.append(i)
#  print(''.join(m))
# print(m)

########Count and display vowels in the given string

# str1=input("enter the line: ")
# count=0
# vowel=['a','e','i','o','u']
# for x in str1:
#     if x in vowel:
#         count=count+1
# #       vowel.append(x)
# # print(''.join(vowel))
# print(count)

#####create  a function to read a text life to the list
def textfile():
    varfile1=open(r"C:\Users\admin\Desktop\testFile1.txt")
    x=varfile1.read()
    print (x)
    print(len(x))
    z=x.split()
    print(len(z))

    y=x.splitlines()
    print(len(y))
    varfile1.close()
textfile()


# list1=[""]
# for line in textfile():
#     list1.append(line.split("are"))
# print(list1)
