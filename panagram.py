def is_pangram(s):
    # Convert the input string to lowercase to ignore case
    s = s.lower()
    
    # Create a set to store unique letters
    unique_letters = set()
    
    # Iterate through the characters in the string
    for char in s:
        if char.isalpha():  # Check if the character is a letter
            unique_letters.add(char)
    
    # Check if the set contains all 26 letters of the English alphabet
    if len(unique_letters) == 26:
        return "pangram"
    else:
        return "not pangram"

# Read the input string
s = input().strip()

result = is_pangram(s)
print(result)
