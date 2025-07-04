import numpy as np
import matplotlib.pyplot as plt

# Constants
I0 = 1e-12  # Threshold of human hearing

# Example input: Intensity
I = 1e-6  # You can change this value
L = 10 * np.log10(I / I0)
print(f"Given Intensity: {I:.2e} W/m²")
print(f"Calculated Loudness: {L:.2f} dB")

# OR Example input: Loudness
L2 = 90  # You can change this value
I2 = I0 * 10**(L2 / 10)
print(f"\nGiven Loudness: {L2:.2f} dB")
print(f"Calculated Intensity: {I2:.2e} W/m²")

# Generate graph of L vs I
I_values = np.logspace(-12, 0, 500)
L_values = 10 * np.log10(I_values / I0)

plt.plot(I_values, L_values)
plt.xscale("log")
plt.xlabel("Intensity (W/m²)")
plt.ylabel("Loudness (dB)")
plt.title("Decibel Scale: Loudness vs Intensity")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

# Highlight calculated point
plt.axvline(I, color='red', linestyle='--', label=f"I = {I:.2e}")
plt.axhline(L, color='green', linestyle='--', label=f"L = {L:.2f} dB")
plt.legend()
plt.show()
