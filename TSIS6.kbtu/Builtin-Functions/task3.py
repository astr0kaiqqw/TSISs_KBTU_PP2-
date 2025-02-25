def is_palindrome(s):
    return s == s[::-1]

word = "madam"
print(f"'{word}' палиндром? {is_palindrome(word)}")

word2 = "hello"
print(f"'{word2}' палиндром? {is_palindrome(word2)}")