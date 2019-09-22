#Mode
'''

a - append
r - read
t - text
x - create
w - write
b - binary
'''

#
# varFile = open(r"C:\Users\admin\Desktop\testFile.txt")
#
# x = varFile.read()
# # y = varFile.readline()
#
# print(x.count('e'))
#
#
# varFile.close()


try:
    varFile = open(r"C:\Users\admin\Desktop\testFile.txt",'r')

    x = varFile.read()
    varFile.close()
    print(x)

    varWrite =  open(r"C:\Users\admin\Desktop\testFile.txt",'w')
    y = x.replace("second line","This is the new line entered in the file")
    varWrite.write(y)
    # print(y)
except:
    print("No such file available")
finally:
    varWrite.close()


# varFile = open(r"C:\Users\admin\Desktop\testFile.txt",'a')
# varFile.write('\nthis is in append mode')
# varFile.close()
#
#
# varFile = open(r"C:\Users\admin\Desktop\testFile1.txt",'x')
# varFile.close()


