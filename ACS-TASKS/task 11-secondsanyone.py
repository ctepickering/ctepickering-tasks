# changes time in hours mins seconds format into number of seconds

usertime= input("Please enter a time in 'hrs:mins:secs' format: ")

#splits hours mins secs
split_time=usertime.split(":")

#checks if the input format is correct
if len(split_time) != 3:
    print("Invalid input. Please use 'hrs:mins:secs' format.")
else :
    hours = int(split_time[0])
    minutes = int(split_time[1])
    seconds = int(split_time[2])

    #calculates the total number of seconds
    totalseconds = (hours * 3600) + (minutes * 60) + seconds

    print("Total seconds:", totalseconds)
#end if