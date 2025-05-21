from caesar_cipher import encrypt_caesar
from monoalphabetic_cipher import encrypt_monoalphabetic

# Patró: per exemple alternar Caesar i Monoalphabetic
pattern = ['caesar', 'mono']

def polyalphabetic_encrypt(text, pattern):
    encrypted_text = ""
    mono_key = None  # guardem clau mono per reutilitzar
    for idx, char in enumerate(text):
        if char.isalpha():
            cipher_type = pattern[idx % len(pattern)]
            if cipher_type == 'caesar':
                encrypted_text += encrypt_caesar(char, shift=5)
            elif cipher_type == 'mono':
                encrypted_char, mono_key = encrypt_monoalphabetic(char.lower(), mono_key)
                encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text, mono_key

if __name__ == "__main__":
    message = "Eduard encriptacio"
    encrypted_message, used_key = polyalphabetic_encrypt(message, pattern)
    print("Missatge original:", message)
    print("Missatge xifrat polialfabètic:", encrypted_message)
    print("Clau monoalfabètica utilitzada:", used_key)


