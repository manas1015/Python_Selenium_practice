def div(a,b):
    try:
        c=a/b
        print(c)
    # except ZeroDivisionError:
    #     print(ZeroDivisionError)
    except Exception:
        print(Exception)
    finally:
        print("Hi I am here")
div(5,5)
print("end of Prog.")


# try:
#  text=input("enter something..")
# except EOFError:
#     print("why did you do an EOFon me")
# except KeyboardInterrupt:
#     print("you canselled the operation")
# else:
#     print('you entered {}'.format(text))
