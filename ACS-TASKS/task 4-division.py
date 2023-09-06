#divides one number by another and outputs the answer and remainder
integer = int(input("Please enter the integer (the number that will be divided): "))
divisor = int(input("Please enter the divisor (the number that will divide the integer): "))
answer = integer // divisor
remainder = integer % divisor
print(str(answer)+ " remainder " + str(remainder))