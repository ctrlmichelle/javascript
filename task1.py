base = float(input("Enter base: "))
height = float(input("Enter height: "))
def calculate_triangle_area(b, h):
    return 0.5 * b * h

print(f"Area: {calculate_triangle_area(base, height)}")