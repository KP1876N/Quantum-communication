import numpy as np

n = 20

alice_bits = np.random.randint(0, 2, n)

alice_bases = np.random.randint(0, 2, n)

print("Alice's Bits:  ", alice_bits)
print("Alice's Bases: ", alice_bases)

print("\nAlice's transmission:")

for i in range(n):
    basis = "+" if alice_bases[i] == 0 else "x"
    print(f"Position {i+1}: Bit = {alice_bits[i]}, Basis = {basis}")
