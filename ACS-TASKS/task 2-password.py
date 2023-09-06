#makes sure user enters a passowrd over 6 characters
password = input("Please enter a password over 6 characters : ")
if len(password) >= 6 :
    print("Valid Password")
else :
    print("Invalid Password")
# end if