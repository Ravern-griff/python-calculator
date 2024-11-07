number_1=input("what is the first number ")
operation=input("what do you what to do ")
number_2=input("what is the second number ")
number_1=(int(number_1))#changes the data type
number_2=(int(number_2))#changes the data type

#adds both numbers
if operation == ("+"):
    answer=(number_1+number_2)
    print(answer)
#subtracks both numbers
elif operation == ("-"):
    answer=(number_1-number_2)
    print (answer)
#devideds both numbers
elif operation == ("/"):
    answer=(number_1/number_2)
    print(answer)
#times both numbers
elif operation == ("*"):
    answer=(number_1*number_2)
    print(answer)
#error mesages
else:
    print ("ERROR")
