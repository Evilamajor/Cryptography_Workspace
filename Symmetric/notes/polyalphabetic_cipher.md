# Polyalphabetic Cipher

A polyalphabetic cipher is a cipher based on substitution, using multiple substitution alphabets. The Vigenère cipher is a well-known example of a polyalphabetic cipher. This type of cipher is more secure than monoalphabetic ciphers because the same letter can be encoded differently depending on its position in the text.

## How It Works

In a polyalphabetic cipher, multiple substitution alphabets are used to encrypt the plaintext. The choice of alphabet for each letter in the plaintext is determined by a keyword or key phrase. The Vigenère cipher, for example, uses a keyword to determine the shift for each letter.

## Example

Using the Vigenère cipher with the keyword "KEY", the word "HELLO" would be encrypted as follows:

- H shifted by K (10 positions) becomes R
- E shifted by E (4 positions) becomes I
- L shifted by Y (24 positions) becomes J
- L shifted by K (10 positions) becomes V
- O shifted by E (4 positions) becomes S

The encrypted text is "RIJVS".
