def divisible_by_3_and_4(n):
    for num in range(n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print("Numbers divisible by 3 and 4:", list(divisible_by_3_and_4(n)))
