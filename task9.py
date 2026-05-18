prods = [['omo', '30kshs', '300'], ['milk', '50kshs', '200'], ['bread', '45kshs', '359'], ['coffee', '5kshs', '79']]
def calculate_total_stock(products_list):
    total = 0
    for item in products_list:
        total += int(item[-1])
    return total

print(f"Total stock: {calculate_total_stock(prods)}")