 # List , Dictionaries,

# collection and efficient storage and retrival of the data
fruitList = ['mango', 'grapes', 'banana', 'jackfruit', 444, 12.22, True, 2+3j]
# print(fruitList)
#
# for item in fruitList:
#     print(item)



# fruitList.append('orange')
# listLength = len(fruitList)
# print(fruitList[listLength-1])
#
#
# del fruitList[3]
#
# print(fruitList)

# numberList = [5, 4, 2, 8,1 ]
# print(numberList)
# numberList.sort(reverse=True)
#
# print(numberList)



anyName = {
    'balaji': 'balaji@gmail.com',
    'faizal':'faizal@gmail.com',
    'john': 'john@gmail.com'
}


del anyName['balaji']

for key, value in anyName.items():
    # print('contact '+ key + ' @ ' + value)
    print('contact {} @ {}'.format(key.capitalize(), value))