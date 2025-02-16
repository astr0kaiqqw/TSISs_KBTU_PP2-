def even_number_generator(n):
    for num in range(0, n + 1, 2):
        yield num

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(", ".join(map(str, even_number_generator(n))))