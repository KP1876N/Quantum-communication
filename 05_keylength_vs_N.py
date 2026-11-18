
import numpy as np
import matplotlib.pyplot as plt

# Different transmission sizes
N_values = [100, 500, 1000, 2000, 5000, 10000, 20000]

# Number of simulations for each N
trials = 200

average_key_lengths = []

for N in N_values:

    key_lengths = []

    for _ in range(trials):

        # Alice generates random bases
        alice_bases = np.random.randint(0, 2, N)

        # Bob generates random bases
        bob_bases = np.random.randint(0, 2, N)

        # Count matching bases
        matching = np.sum(alice_bases == bob_bases)

        key_lengths.append(matching)

    # Calculate average sifted key length
    average_key_lengths.append(np.mean(key_lengths))

# Theoretical expected key length
theoretical_lengths = np.array(N_values) / 2

# Print results
print("N value | Average sifted key length")

for N, length in zip(N_values, average_key_lengths):
    print(f"{N:6d}  | {length:.2f}")

# Plot the graph
plt.plot(
    N_values, average_key_lengths,
    marker="o", label="Simulated average"
)

plt.plot(
    N_values, theoretical_lengths,
    linestyle="--", label="Theoretical N/2"
)

plt.xlabel("Number of transmitted bits (N)")
plt.ylabel("Sifted key length")
plt.title("BB84: Sifted Key Length vs N")
plt.legend()
plt.grid(True)

plt.show()
