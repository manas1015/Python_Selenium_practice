# varDict = {
#     'balaji':'balaji@gmail.com',
#     'mobile': 43533353,
#     'Age': '30',
#     'emptyKey': '  '
# }

# print(type(varDict))

# varDict['balaji'] = 'balaji@gmail.com'
# varDict['mobile'] = 32323232
# varDict[21] = True


# print(varDict['mobile'])
#
# print(len(varDict))

#
# for x in varDict:
#     print(x)

# for varKey, varValue in varDict.items():
#     print(varKey , varValue)


# for varOnlyValue in varDict.keys():
#     if varOnlyValue.lower()=='age':
#         print(varDict[varOnlyValue])

# del varDict['emptyKey']

# varDict.pop('mobile')
# varDict.popitem()



# varDict['Age'] = 31
#
# print(varDict)
#
# varCopyDic = varDict.copy()
# print(varCopyDic)

# varDict1={}
# print(varDict1)

varDict2={'Name':'Manas' ,'Email':'mdmanas1015','mobile':'8056080670'}
# print(varDict2)
# print(len(varDict2))
# print(varDict2["Email"])
# for x,y in varDict2.items():
#     if 'Name1' ==x and 'Manas'==y:
#         print(x,y)
#     else:
#         print("failed")
#         break

# x=varDict2["Name"]
# print(x)
# x=varDict2.get("Email")
# print(x)

# varDict2["mobile"]= 1111111
# print(varDict2)

# for x in varDict2:
#     print(x)
# for x in varDict2:
#     print(varDict2[x])
#
# for x in varDict2.values():
#     print(x)

# varDict2["address"]='odisha'
# print(varDict2)


# for x,y in varDict2.items():
#     print(x,y)

# varDict2.pop("address")
# print(varDict2)
#
# varDict2.popitem()
# print(varDict2)

varDict2.update({"age":'32'})
print(varDict2)

x=varDict2.keys()
print(x)