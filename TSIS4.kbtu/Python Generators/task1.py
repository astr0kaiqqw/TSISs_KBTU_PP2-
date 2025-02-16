def square_generator(N):
    for num in range(N + 1):
        yield num ** 2

if __name__ == "__main__":
    N = int(input("Enter a number: "))
    for square in square_generator(N):
        print(square)
