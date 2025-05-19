from collections import Counter
import string

def frequency_analysis(text):
    text = text.lower()
    # Només analitzem caràcters alfabètics
    filtered_text = [char for char in text if char in string.ascii_lowercase]

    frequency = Counter(filtered_text)
    total_chars = sum(frequency.values())

    # Calcula les freqüències relatives
    freq_relative = {char: (count / total_chars) for char, count in frequency.items()}

    # Ordena per freqüència descendent
    sorted_freq = dict(sorted(freq_relative.items(), key=lambda item: item[1], reverse=True))

    return sorted_freq

# Test ràpid
if __name__ == "__main__":
    encrypted_text = "Khoor, Hgxdug!"
    frequencies = frequency_analysis(encrypted_text)

    print("Anàlisi freqüencial del text xifrat:")
    for char, freq in frequencies.items():
        print(f"{char}: {freq:.2%}")


