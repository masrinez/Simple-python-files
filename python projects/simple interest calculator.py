principal = float(input("Enter the principal: "))

rate = float(input("\nEnter the rate: "))

time = float(input("\nEnter the time: "))

amount = ((1 + (rate * time)) / 100) * principal

print(f"\nYour total amount is: " + str(amount))

res = "1"

while res == "1":
    print("\nThis is a simple interest calculator")

    res = input("\npress (1) to continue:")

    if res != "1":
        break
