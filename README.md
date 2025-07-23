# EEG-Tensor-Decomposition
# CP Decomposition on Simulated EEG Data

This repository demonstrates how to apply Canonical Polyadic (CP) decomposition on simulated EEG data using the `tensorly` library in Python.

## 📊 Description

We simulate a 3D tensor with dimensions:
- `32` EEG channels
- `100` time points
- `20` trials

Then we apply CP decomposition (rank = 3) to extract component patterns across:
- Channels
- Time
- Trials

## 🧠 Why Use CP Decomposition?

CP decomposition helps uncover **latent structure** in multidimensional datasets like EEG, MEG, or fMRI. It's useful for:
- Identifying spatial-temporal patterns
- Dimensionality reduction
- Preprocessing for machine learning

## 📁 Files

- `cp_decomposition_eeg.py` — main script
- `cp_decomposition_eeg.ipynb` — notebook version (interactive)
- `README.md` — you're reading it

## 📦 Dependencies

```bash
pip install numpy matplotlib tensorly
