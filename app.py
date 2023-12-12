# Sample app file

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a ** b

def subtract_numbers(a, b):
    return a - b

def main():
    x = 5
    y = 3
    sum_result = add_numbers(x, y)
    product_result = multiply_numbers(x, y)

    print(f"Sum: {sum_result}")
    print(f"Product: {product_result}")

if __name__ == "__main__":
    main()
