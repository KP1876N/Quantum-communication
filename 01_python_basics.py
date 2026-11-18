
import numpy as np

# Generate 1000 random binary bits
bits = np.random.randint(0, 2, 1000)

# Count zeros and ones
zeros = np.count_nonzero(bits == 0)
ones = np.count_nonzero(bits == 1)

print("First 20 bits:", bits[:20])
print("Total bits:", len(bits))
print("Number of zeros:", zeros)
print("Number of ones:", ones)
