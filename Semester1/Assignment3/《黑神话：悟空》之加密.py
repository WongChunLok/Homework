def decrypt_caesar(k, s):
    decrypted_text = []

    for char in s:
        if 'a' <= char <= 'z':
            decrypted_char = chr((ord(char) - ord('a') - k) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            decrypted_char = chr((ord(char) - ord('A') - k) % 26 + ord('A'))
        else:
            decrypted_char = char  
        decrypted_text.append(decrypted_char)

    return ''.join(decrypted_text)


k = int(input())
s = input()

print(decrypt_caesar(k, s))