import os

def check_access(path):
    print(f"Путь '{path}' существует?", os.path.exists(path))
    print(f"Можно читать?", os.access(path, os.R_OK))
    print(f"Можно писать?", os.access(path, os.W_OK))
    print(f"Можно выполнить?", os.access(path, os.X_OK))


check_access("test.txt")
