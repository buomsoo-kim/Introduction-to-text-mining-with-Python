def vowel(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = list(s)
    c = 0
    for alphabet in s:
        if alphabet in vowels:
            c += 1
    return c

print(vowel('apples'))
print(vowel('Her name is Jane'))