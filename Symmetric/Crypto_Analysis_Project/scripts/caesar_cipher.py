def caesar_encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    return caesar_encrypt(encrypted_text, -shift)

# Test ràpid
if __name__ == "__main__":
    test_text = "Hello, Eduard!"
    shift = 3
    encrypted = caesar_encrypt(test_text, shift)
    decrypted = caesar_decrypt(encrypted, shift)

    print(f"Original: {test_text}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")


