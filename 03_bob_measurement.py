
import numpy as np

# Number of photons
n = 20

# Alice's random bits and bases
alice_bits = np.random.randint(0, 2, n)
alice_bases = np.random.randint(0, 2, n)

# Bob independently chooses random measurement bases
bob_bases = np.random.randint(0, 2, n)

# Simulate Bob's measurements
bob_bits = np.zeros(n, dtype=int)

for i in range(n):

    if alice_bases[i] == bob_bases[i]:
        # Same basis: Bob gets Alice's original bit
        bob_bits[i] = alice_bits[i]

    else:
        # Different basis: measurement result is random
        bob_bits[i] = np.random.randint(0, 2)

print("Alice's bits:  ", alice_bits)
print("Alice's bases: ", alice_bases)
print("Bob's bases:   ", bob_bases)
print("Bob's results: ", bob_bits)
