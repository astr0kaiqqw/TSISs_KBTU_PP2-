def countdown(n):
    for num in range(n, -1, -1):
        yield num

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    
    for number in countdown(n):
        print(number)