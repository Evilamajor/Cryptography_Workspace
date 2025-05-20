import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from collections import Counter
from caesar_cipher import encrypt_caesar, decrypt_caesar
from monoalphabetic_cipher import encrypt_monoalphabetic, decrypt_monoalphabetic

# Funció per anàlisi de freqüències
def frequency_analysis(text):
    text = text.replace(" ", "").lower()
    total_chars = len(text)
    frequencies = Counter(text)
    freq_relativa = {char: (count / total_chars) * 100 for char, count in frequencies.items()}
    freq_df = pd.DataFrame(freq_relativa.items(), columns=['Character', 'Frequency (%)']).sort_values(by='Frequency (%)', ascending=False)
    return freq_df

# Configuració visual
sns.set(style='whitegrid', palette='muted', font_scale=1.2)

# Text per defecte
original_text = "Hello, Eduard!"

# Caesar Cipher
caesar_encrypted = encrypt_caesar(original_text, shift=3)
caesar_freq = frequency_analysis(caesar_encrypted)

# Monoalphabetic Cipher
mono_encrypted, key_used = encrypt_monoalphabetic(original_text.lower())
mono_freq = frequency_analysis(mono_encrypted)

# Creació de directoris automàticament
os.makedirs("../plots", exist_ok=True)

# Visualització gràfica
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Caesar Cipher plot
sns.barplot(ax=axes[0], x='Character', y='Frequency (%)', data=caesar_freq)
axes[0].set_title('Caesar Cipher Frequency Analysis')

# Monoalphabetic Cipher plot
sns.barplot(ax=axes[1], x='Character', y='Frequency (%)', data=mono_freq)
axes[1].set_title('Monoalphabetic Cipher Frequency Analysis')

plt.tight_layout()

# Guardar els gràfics automàticament
fig.savefig("../plots/cipher_analysis.png")
print("✅ Anàlisi automatitzada completada! Gràfics guardats a ../plots/cipher_analysis.png")


