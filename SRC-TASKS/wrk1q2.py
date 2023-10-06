MAX=12
name_array=["" for _ in range(MAX)]
name_array[11]="bob"
search_name=input("Please enter the student name you are looking for:")
found = False
i =0
while not found and i<MAX:
    if search_name==name_array[i]:
        found==True
        i = i +1
    #endif
#endwhile
if found:
    print("The students index number is", i +1)
else:
    print("Name not found")
#endif