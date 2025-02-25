import os

def path_info(path):
    if os.path.exists(path):
        print(f"Путь '{path}' существует!")
        print(f"Имя файла: {os.path.basename(path)}")
        print(f"Директория: {os.path.dirname(path)}")
    else:
        print("Путь не существует.")


path_info("C:/Users/test.txt")
