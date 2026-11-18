import numpy as np

N = 20

alice_bits = np.random.randint(0, 2, N)
alice_bases = np.random.randint(0, 2, N)

bob_bases = np.random.randint(0, 2, N)

bob_bits = np.zeros(N, dtype=int)

for i in range(N):
    if alice_bases[i] == bob_bases[i]:
        bob_bits[i] = alice_bits[i]
    else:
        bob_bits[i] = np.random.randint(0, 2)

matching_positions = (alice_bases == bob_bases)

alice_sifted_key = alice_bits[matching_positions]
bob_sifted_key = bob_bits[matching_positions]

key_length = len(alice_sifted_key)

print("Alice's bits:       ", alice_bits)
print("Alice's bases:      ", alice_bases)
print("Bob's bases:        ", bob_bases)
print("Bob's results:      ", bob_bits)

print("\nMatching positions: ", matching_positions)
print("Alice's sifted key: ", alice_sifted_key)
print("Bob's sifted key:   ", bob_sifted_key)

print("\nTotal bits sent:    ", N)
print("Sifted key length:  ", key_length)
print("Keys match:         ", np.array_equal(
    alice_sifted_key, bob_sifted_key
))
