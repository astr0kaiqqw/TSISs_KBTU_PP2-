def count_lines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        return len(lines)


print("Количество строк:", count_lines("example.txt"))
