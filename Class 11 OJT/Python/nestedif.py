user = input ("Enter username : ")

if user == "admin":
    print("You are successfully loged in, in admin's dasboard")
    attendence = input("Enter attendence : ")
    if attendence == "Full":
        print("Stuff attendence is full")
    elif attendence =="Half":
         print("Stuff attendence is half")
    elif attendence == "Morning":
         print("Stuff attendence is morning")
    else:
          print("Stuff is absent")
else:
    print("You are not the admin")