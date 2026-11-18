import numpy as np

N = 10000

noise_probability = 0.05

alice_bits = np.random.randint(0, 2, N)
alice_bases = np.random.randint(0, 2, N)

bob_bases = np.random.randint(0, 2, N)

bob_bits = np.zeros(N, dtype=int)

for i in range(N):
    if alice_bases[i] == bob_bases[i]:
        bob_bits[i] = alice_bits[i]
    else:
        bob_bits[i] = np.random.randint(0, 2)

noise = np.random.random(N) < noise_probability
bob_bits[noise] = 1 - bob_bits[noise]

matching = (alice_bases == bob_bases)

alice_key = alice_bits[matching]
bob_key = bob_bits[matching]

errors = np.sum(alice_key != bob_key)

qber = (errors / len(alice_key)) * 100

print("Transmitted bits:", N)
print("Noise probability:", noise_probability * 100, "%")
print("Sifted key length:", len(alice_key))
print("Number of errors:", errors)
print("QBER:", round(qber, 2), "%")
