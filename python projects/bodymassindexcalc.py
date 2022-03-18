height = float(input("\nEnter height(in Metres): "))

weight = float(input("\nEnter weight(in KiloGrams): "))

bmi = weight / (height * height)

print("\nYour BMI is:- " + str(bmi))

if (bmi >= 1.0) and (bmi <= 16):
    print("\nYou are severely underweight, please visit the dietician.")

elif (bmi >= 16.1) and (bmi <= 18.5):
    print("\nYou are underweight, please visit the dietician.")

elif (bmi >= 18.6) and (bmi <= 25.0):
    print("\nYou are normal, keep it up.!")

elif (bmi >= 25.1) and (bmi <= 30.0):
    print("\nYou are overweight, please watch your calories intake.")

else:
    print("\nYou are obese, please visit the hospital.")

res = "1"

while res == "1":
    print("\nHello, thank you for using our BMI calculator, please refresh for a new calculation")

    res = input("\nPress (1) to continue:")

    if res != "1":
        break

print("\nThank you, Goodbye.!")
