#2 numbers input, outputs highest then second highest number
num1 = int(input("please enter a first number "))
num2 = int(input("please enter a different second number "))
if num1 > num2 :
    print(str(num1)+", "+ (str(num2)))
else :
    print(str(num2)+", "+ (str(num1)))