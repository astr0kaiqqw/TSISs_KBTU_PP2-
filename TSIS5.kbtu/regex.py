import re

# Чтение содержимого файла row.txt
with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 1. Найти строку, содержащую 'a', за которой следует 0 или более 'b'
def match_a_followed_by_b(string):
    return bool(re.fullmatch(r'ab*', string))

# 2. Найти строку, содержащую 'a', за которой следует от 2 до 3 'b'
def match_a_followed_by_2_to_3_b(string):
    return bool(re.fullmatch(r'ab{2,3}', string))

# 3. Найти последовательности строчных букв, соединенных символом '_'
def find_lowercase_with_underscore(string):
    return re.findall(r'\b[a-z]+_[a-z]+\b', string)

# 4. Найти последовательности одной заглавной буквы, за которой следуют строчные

def find_upper_followed_by_lower(string):
    return re.findall(r'[A-Z][a-z]+', string)

# 5. Найти строку, начинающуюся на 'a', за которой идут любые символы, и заканчивается на 'b'
def match_a_anything_b(string):
    return bool(re.fullmatch(r'a.*b', string))

# 6. Заменить все пробелы, запятые и точки на ':'
def replace_with_colon(string):
    return re.sub(r'[ ,.]', ':', string)

# 7. Преобразовать snake_case в CamelCase
def snake_to_camel(string):
    return ''.join(word.capitalize() for word in string.split('_'))

# 8. Разделить строку по заглавным буквам
def split_by_uppercase(string):
    return re.split(r'(?=[A-Z])', string)

# 9. Вставить пробелы между словами, начинающимися с заглавных букв
def insert_spaces_capitals(string):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', string)

# 10. Преобразовать CamelCase в snake_case
def camel_to_snake(string):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', string).lower()

# Применение функций к содержимому row.txt
print(match_a_followed_by_b(text))
print(match_a_followed_by_2_to_3_b(text))
print(find_lowercase_with_underscore(text))
print(find_upper_followed_by_lower(text))
print(match_a_anything_b(text))
print(replace_with_colon(text))
print(snake_to_camel(text))
print(split_by_uppercase(text))
print(insert_spaces_capitals(text))
print(camel_to_snake(text))
