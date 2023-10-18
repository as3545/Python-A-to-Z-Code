def caesarCipher(s, k):
    encryptedString = ""

    for c in s:
        if c.isalpha():
            base = 'a' if c.islower() else 'A'
            encryptedChar = chr(ord(base) + (ord(c) - ord(base) + k) % 26)
            encryptedString += encryptedChar
        else:
            encryptedString += c  # Non-alphabet characters remain unchanged

    return encryptedString

def main():
    n = int(input())
    s = input()
    k = int(input())

    result = caesarCipher(s, k)
    print(result)

if __name__ == "__main__":
    main()
