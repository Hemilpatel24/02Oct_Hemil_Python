sub1 = int(input("Enter marks of sub1:"))
sub2 = int(input("Enter marks of sub2:"))
sub3 = int(input("Enter marks of sub3:"))
sub4 = int(input("Enter marks of sub4:"))

if sub1>=40 and sub2>=40 and sub3>=40 and sub4>=40:

    totalmarks = sub1 + sub2 + sub3 + sub4
    print("Total Marks are:", totalmarks)
    percentage = (totalmarks/400)*100
    print("Your Percentage:",percentage)

    if percentage >= 70:
        print("Paased with Distinction.")
    elif percentage >= 60:
        print("passed with First Class.")
    elif percentage >= 50:
        print("Passed with Second Class.")
    elif percentage >= 40:
        print("Passed with Pass Class.")
    else:
        print("Sorry...You FAILED!")
else:
    print("FAILED!")


