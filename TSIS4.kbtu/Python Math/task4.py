def parallelogram_area(base, height):
    return base * height

if __name__ == "__main__":
    base = float(input("Length of base: "))
    height = float(input("Height of parallelogram: "))
    
    area = parallelogram_area(base, height)
    print("Expected Output:", area)