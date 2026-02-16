import numpy as np

np.random.seed(42)

def parallel_tempering(N, q, max_steps, T_ladder):
    replicas = len(T_ladder)
    states = [np.random.randint(0, q, N) for _ in range(replicas)]
    targets = np.random.randint(0, q, N)
    
    for step in range(max_steps):
        for r in range(replicas):
            i = np.random.randint(0, N)
            old_val = states[r][i]
            new_val = np.random.randint(0, q)
            delta_E = abs(new_val - targets[i]) - abs(old_val - targets[i])
            if delta_E <= 0 or np.random.rand() < np.exp(-delta_E / T_ladder[r]):
                states[r][i] = new_val
        
        if step % 100 == 0:
            for r in range(replicas - 1):
                E1 = energy(states[r], targets)
                E2 = energy(states[r+1], targets)
                T1, T2 = T_ladder[r], T_ladder[r+1]
                swap_prob = min(1, np.exp((1/T1 - 1/T2) * (E2 - E1)))
                if np.random.rand() < swap_prob:
                    states[r], states[r+1] = states[r+1].copy(), states[r].copy()
    
    final_E = min(energy(s, targets) for s in states)
    return final_E
