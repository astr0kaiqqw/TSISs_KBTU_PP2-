import re


with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()


def match_a_followed_by_b(string):
    return bool(re.fullmatch(r'ab*', string))


def match_a_followed_by_2_to_3_b(string):
    return bool(re.fullmatch(r'ab{2,3}', string))


def find_lowercase_with_underscore(string):
    return re.findall(r'\b[a-z]+_[a-z]+\b', string)



def find_upper_followed_by_lower(string):
    return re.findall(r'[A-Z][a-z]+', string)


def match_a_anything_b(string):
    return bool(re.fullmatch(r'a.*b', string))


def replace_with_colon(string):
    return re.sub(r'[ ,.]', ':', string)


def snake_to_camel(string):
    return ''.join(word.capitalize() for word in string.split('_'))

def split_by_uppercase(string):
    return re.split(r'(?=[A-Z])', string)


def insert_spaces_capitals(string):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', string)


def camel_to_snake(string):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', string).lower()


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
