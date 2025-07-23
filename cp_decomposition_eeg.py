"""
CP Decomposition on Simulated EEG Data
Author: Burcu Tutuk
Date: July 2025

This script demonstrates how to apply Canonical Polyadic (CP) decomposition
on a simulated EEG tensor (channels x time x trials) using TensorLy.
"""

# --- Import libraries ---
import numpy as np
import tensorly as tl
from tensorly.decomposition import parafac
import matplotlib.pyplot as plt

# --- Set random seed for reproducibility ---
np.random.seed(0)

# --- Simulate EEG-like data ---
# Dimensions: 32 channels x 100 time points x 20 trials
channels, time_points, trials = 32, 100, 20
tensor_data = np.random.rand(channels, time_points, trials)

# --- Convert data to tensorly tensor ---
tensor = tl.tensor(tensor_data)

# --- Apply CP decomposition with rank=3 ---
rank = 3
weights, factors = parafac(tensor, rank=rank, return_weights=True)
channel_factors, time_factors, trial_factors = factors

# --- Plot temporal components ---
plt.figure(figsize=(10, 5))
for i in range(rank):
    plt.plot(time_factors[:, i], label=f'Component {i+1}')
plt.title('Temporal Components from CP Decomposition')
plt.xlabel('Time Points')
plt.ylabel('Component Activation')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
