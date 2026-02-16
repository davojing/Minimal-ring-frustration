import numpy as np

np.random.seed(42)

def temperature_gradient(N, T_min, T_max):
    return np.linspace(T_min, T_max, N)

def metropolis_step_gradient(state, targets, T_node):
    i = np.random.randint(0, len(state))
    old_val = state[i]
    new_val = np.random.randint(0, q)
    delta_E = abs(new_val - targets[i]) - abs(old_val - targets[i])
    T = T_node[i]
    if delta_E <= 0 or np.random.rand() < np.exp(-delta_E / T):
        state[i] = new_val
