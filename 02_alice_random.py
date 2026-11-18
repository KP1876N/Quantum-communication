
import numpy as np

# Number of bits Alice wants to transmit
n = 20

# Generate random bits: 0 or 1
alice_bits = np.random.randint(0, 2, n)

# Generate random bases: 0 = Rectilinear (+)
#                         1 = Diagonal (x)
alice_bases = np.random.randint(0, 2, n)

print("Alice's Bits:  ", alice_bits)
print("Alice's Bases: ", alice_bases)

print("\nAlice's transmission:")

for i in range(n):
    basis = "+" if alice_bases[i] == 0 else "x"
    print(f"Position {i+1}: Bit = {alice_bits[i]}, Basis = {basis}")
