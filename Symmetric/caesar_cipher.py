def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Example Usage:
message = "Cryptography"
shift = 3
encrypted = caesar_cipher(message, shift)
decrypted = caesar_cipher(encrypted, -shift)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)

