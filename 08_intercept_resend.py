import numpy as np

N = 10000

alice_bits = np.random.randint(0, 2, N)
alice_bases = np.random.randint(0, 2, N)

eve_bases = np.random.randint(0, 2, N)

eve_bits = np.zeros(N, dtype=int)

for i in range(N):
    if alice_bases[i] == eve_bases[i]:
        eve_bits[i] = alice_bits[i]
    else:
        eve_bits[i] = np.random.randint(0, 2)

bob_bases = np.random.randint(0, 2, N)

bob_bits = np.zeros(N, dtype=int)

for i in range(N):
    if eve_bases[i] == bob_bases[i]:
        bob_bits[i] = eve_bits[i]
    else:
        bob_bits[i] = np.random.randint(0, 2)

matching = (alice_bases == bob_bases)

alice_key = alice_bits[matching]
bob_key = bob_bits[matching]

errors = np.sum(alice_key != bob_key)

qber = (errors / len(alice_key)) * 100

print("Total transmitted photons:", N)
print("Sifted key length:", len(alice_key))
print("Number of errors:", errors)
print("QBER:", round(qber, 2), "%")
