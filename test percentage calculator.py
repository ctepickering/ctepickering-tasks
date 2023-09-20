marks=input("Please enter your test score: ")
testscore=marks.split("/")
percantage = (int(testscore[0])/int(testscore[1]))*100
print("You scored " + str(percantage)+"%")