# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

def reverse_words(text):
    return text[::-1]

print(reverse_words('The quick brown fox jumps over the lazy dog.'))

print(reverse_words("double  spaces"))