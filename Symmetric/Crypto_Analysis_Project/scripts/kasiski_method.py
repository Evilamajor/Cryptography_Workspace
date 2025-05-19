from collections import defaultdict

def kasiski_examination(ciphertext, seq_length=3):
    sequences = defaultdict(list)

    # Cerca seqüències repetides i les seves posicions
    for i in range(len(ciphertext) - seq_length + 1):
        seq = ciphertext[i:i+seq_length]
        sequences[seq].append(i)

    # Guarda només seqüències que apareixen més d'una vegada
    repeated_seqs = {seq: positions for seq, positions in sequences.items() if len(positions) > 1}

    # Calcula distàncies entre seqüències repetides
    seq_distances = {seq: [positions[i+1] - positions[i] for i in range(len(positions)-1)] 
                     for seq, positions in repeated_seqs.items()}

    return repeated_seqs, seq_distances

# Test ràpid
if __name__ == "__main__":
    cipher_text = "ABXABCABYABCABZABC"  # exemple senzill amb repeticions clares
    repeated_seqs, distances = kasiski_examination(cipher_text)

    print("Seqüències repetides i posicions:")
    for seq, pos in repeated_seqs.items():
        print(f"{seq}: {pos}")

    print("\nDistàncies entre repeticions:")
    for seq, dist in distances.items():
        print(f"{seq}: {dist}")


