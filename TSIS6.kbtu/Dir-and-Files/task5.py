def write_list_to_file(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines("\n".join(data))


my_list = ["Python", "Java", "C++"]
write_list_to_file("languages.txt", my_list)
