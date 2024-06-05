#expection -> an event occurs to distrupt the noraml flow of operation

# try:
#     age = int(input("Enter your age: "))
#     print(age)

# except:
#     print("Kindly enter numerical value")

# print("My name is *Your name*")

#----------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------#

# 2 ta error aayo vhani like eg here...

# try:
#     a = int(input("Enter the first num: "))
#     b = int(input("Enter the second num: "))
#     c = a/b
# except ValueError:
#     print('kindly enter a numeric value')
# except ZeroDivisionError:
#     print('Zero can not be divided by other number')
# else:
#     print('The value is', c)

#----------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------#

def login():
    user = 'admin'
    pass1 = 'admin'
    try:
        username = input("Enter a username = ")
        password = input("Enter a password = ")

        if user !=username:
            raise ZeroDivisionError
        elif pass1 != password:
            raise ValueError
        
    except ZeroDivisionError:
        print("Username invalid")
        login()
    except ValueError:
        print("Password invalid")
        login()
    else:
        print("successfully loged in")
    finally:
        print("Home")

login()

#----------------------------------------------------------------------------------------#

