import random

def _tab_bob_one(dones_password: bool = True) -> bool:
    path_entered = random.choice(['A', 'B'])
    challenge = random.choice(['A', 'B'])

    if dones_password:
        return True
    else:
        return path_entered == challenge

def simulate_ali_baba_trials(trials=20):
    success_count = 0
    for _ in range(trials):
        result = _tab_bob_one(False)  # malicious prover
        if result:
            success_count += 1

    probability = success_count / trials
    print(f"Malicious prover success: {success_count}/{trials}")
    print(f"Success probability: {probability:.2f}")

simulate_ali_baba_trials()
