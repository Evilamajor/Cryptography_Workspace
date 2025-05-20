def encrypt_caesar(text, shift=3):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char.lower()) - 97 + shift_amount) % 26) + 97)
            encrypted_text += new_char.upper() if char.isupper() else new_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar(text, shift=3):
    return encrypt_caesar(text, -shift)

# Opcional (test ràpid)
if __name__ == "__main__":
    original = "Hello, Eduard!"
    encrypted = encrypt_caesar(original, shift=3)
    decrypted = decrypt_caesar(encrypted, shift=3)
    
    print(f"Original: {original}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")



