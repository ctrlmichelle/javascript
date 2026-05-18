speed = float(input("Enter speed: "))
if speed < 70:
    print("Ok")
else:
    points = int((speed - 70) // 5)
    if points > 12:
        print("License suspended")
    else:
        print(f"Points: {points}")