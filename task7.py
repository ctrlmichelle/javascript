marks = float(input("Enter student marks (0-100): "))
if 0 <= marks <= 100:
    if marks > 79: grade = "A"
    elif marks >= 60: grade = "B"
    elif marks >= 49: grade = "C"
    elif marks >= 40: grade = "D"
    else: grade = "E"
    print(f"Grade: {grade}")
else:
    print("Invalid marks entered")