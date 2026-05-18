num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
def find_largest(a, b, c):
    if a >= b and a >= c: return a
    if b >= a and b >= c: return b
    return c

print(f"Largest: {find_largest(num1, num2, num3)}")