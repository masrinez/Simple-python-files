length = float(input("Enter rectangle length: "))

width = float(input("Enter rectangle width: "))

area = length * width

perimeter = (length + width) * 2

print(f"\nThe Area of the rectangle is: " + str(area))

print(f"\nThe perimeter of the rectangle is: " + str(perimeter))

res = "1"

while res == "1":
    print("The area and the perimeter is given above")

    res = input ("press (1) to continue.")



