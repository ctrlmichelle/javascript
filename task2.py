num = int(input("Enter a number: "))
def check_even_odd(n):
    if n % 4 == 0:
        return "divisible by 4"
    return "even" if n % 2 == 0 else "odd"

print(check_even_odd(num))