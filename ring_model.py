•	Name: ring_model.py Paste:
import numpy as np

np.random.seed(42)

def random_state(N, q):
    return np.random.randint(0, q, size=N)

def energy(state, targets):
    return np.sum(np.abs((state - targets) % q))

def metropolis_step(state, targets, T):
    i = np.random.randint(0, len(state))
    old_val = state[i]
    new_val = np.random.randint(0, q)
    delta_E = abs(new_val - targets[i]) - abs(old_val - targets[i])
    if delta_E <= 0 or np.random.rand() < np.exp(-delta_E / T):
        state[i] = new_val
