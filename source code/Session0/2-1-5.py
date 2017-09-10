def search_text(word, char):
    if char in word:
        return word.index(char)
    return False

print(search_text('name', 'a'))
print(search_text('name', 'e'))
print(search_text('jane', 'p'))
print(search_text('jane', 'n'))