count = int(input("\nEnter your score: "))

if (count >= 90) and (count <= 100):
    print("\nYour grade is: A")
    print("\nYour score is: " + str(count))

elif (count >= 80) and (count <= 89):
    print("\nYour grade is: B")
    print("\nYour score is:" + str(count))

elif (count >= 70) and (count <= 79):
    print("\nYour grade is: C")
    print("\nYour score is:" + str(count))

elif (count >= 60) and (count <= 69):
    print("\nYour grade is: D")
    print("\nYour score is: " + str(count))

else:
    print("\nYour grade is: F")
    print("\nYour score is: " + str(count))

res = "1"

while res == "1":
    print("\nHello")

    res = input("\nPress (1) to continue>> ")


    if res != "1":
        break



print("\nThank you for using our grading system")