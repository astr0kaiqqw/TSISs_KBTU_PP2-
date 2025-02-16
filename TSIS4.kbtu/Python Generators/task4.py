def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

if __name__ == "__main__":
    a = int(input("Enter the start number: "))
    b = int(input("Enter the end number: "))
    
    for square in squares(a, b):
        print(square)