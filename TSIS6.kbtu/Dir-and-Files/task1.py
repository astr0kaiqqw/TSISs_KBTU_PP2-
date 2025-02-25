import os

def list_contents(path="."):
    print("Только директории:")
    print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])

    print("\nТолько файлы:")
    print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

    print("\nВсе файлы и папки:")
    print(os.listdir(path))


list_contents("C:/Users")  
