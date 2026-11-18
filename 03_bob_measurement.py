import numpy as np

n = 20

alice_bits = np.random.randint(0, 2, n)
alice_bases = np.random.randint(0, 2, n)

bob_bases = np.random.randint(0, 2, n)

bob_bits = np.zeros(n, dtype=int)

for i in range(n):

    if alice_bases[i] == bob_bases[i]:
        bob_bits[i] = alice_bits[i]

    else:
        bob_bits[i] = np.random.randint(0, 2)

print("Alice's bits:  ", alice_bits)
print("Alice's bases: ", alice_bases)
print("Bob's bases:   ", bob_bases)
print("Bob's results: ", bob_bits)
