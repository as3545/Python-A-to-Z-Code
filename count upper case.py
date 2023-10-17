def camelCase(s):
    word_count = 1  # Initialize with 1 for the first word

    for char in s:
        if char.isupper():
            word_count += 1

    return word_count

# Sample Input
s = input()
result = camelCase(s)
print(result)
