import random
import string

def generate_monoalphabetic_key():
    alphabet = list(string.ascii_lowercase)
    shuffled_alphabet = alphabet[:]
    random.shuffle(shuffled_alphabet)
    return dict(zip(alphabet, shuffled_alphabet))

def encrypt_monoalphabetic(text, key=None):
    if key is None:
        key = generate_monoalphabetic_key()
    
    encrypted = ""
    for char in text:
        if char.lower() in key:
            encrypted_char = key[char.lower()]
            encrypted += encrypted_char.upper() if char.isupper() else encrypted_char
        else:
            encrypted += char
            
    return encrypted, key

def decrypt_monoalphabetic(text, key):
    inverse_key = {v: k for k, v in key.items()}
    decrypted = ""
    for char in text:
        if char.lower() in inverse_key:
            decrypted_char = inverse_key[char.lower()]
            decrypted += decrypted_char.upper() if char.isupper() else decrypted_char
        else:
            decrypted += char
            
    return decrypted

# Opcional (test ràpid)
if __name__ == "__main__":
    original = "hello eduard"
    encrypted, used_key = encrypt_monoalphabetic(original)
    decrypted = decrypt_monoalphabetic(encrypted, used_key)
    
    print(f"Original: {original}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print(f"Key used: {used_key}")

