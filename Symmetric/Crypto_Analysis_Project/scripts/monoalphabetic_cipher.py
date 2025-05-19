import random
import string

# Generar una clau monoalfabètica aleatòria
def generate_monoalphabetic_key():
    alphabet = list(string.ascii_lowercase)
    shuffled_alphabet = alphabet[:]
    random.shuffle(shuffled_alphabet)
    return dict(zip(alphabet, shuffled_alphabet))

# Xifratge monoalfabètic
def monoalphabetic_encrypt(plain_text, key):
    encrypted_text = ""
    for char in plain_text.lower():
        if char in key:
            encrypted_text += key[char]
        else:
            encrypted_text += char
    return encrypted_text

# Desxifratge monoalfabètic
def monoalphabetic_decrypt(encrypted_text, key):
    reverse_key = {v: k for k, v in key.items()}
    decrypted_text = ""
    for char in encrypted_text:
        if char in reverse_key:
            decrypted_text += reverse_key[char]
        else:
            decrypted_text += char
    return decrypted_text

# Test ràpid
if __name__ == "__main__":
    text = "hello eduard"
    key = generate_monoalphabetic_key()

    encrypted = monoalphabetic_encrypt(text, key)
    decrypted = monoalphabetic_decrypt(encrypted, key)

    print(f"Original: {text}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print(f"Key used: {key}")


