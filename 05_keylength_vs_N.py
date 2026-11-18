import numpy as np
import matplotlib.pyplot as plt

N_values = [100, 500, 1000, 2000, 5000, 10000, 20000]

trials = 200

average_key_lengths = []

for N in N_values:

    key_lengths = []

    for _ in range(trials):

        alice_bases = np.random.randint(0, 2, N)

        bob_bases = np.random.randint(0, 2, N)

        matching = np.sum(alice_bases == bob_bases)

        key_lengths.append(matching)

    average_key_lengths.append(np.mean(key_lengths))

theoretical_lengths = np.array(N_values) / 2

print("N value | Average sifted key length")

for N, length in zip(N_values, average_key_lengths):
    print(f"{N:6d}  | {length:.2f}")

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
