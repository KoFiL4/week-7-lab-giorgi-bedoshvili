import random

def ali_baba_once(knows_password: bool = True) -> bool:
    paths = ['A', 'B']
    path_entered = random.choice(paths)      # Alice enters randomly
    challenge = random.choice(paths)         # Bob challenges randomly

    if knows_password:
        success = True
    else:
        success = (path_entered == challenge)

    print(f"Alice entered: {path_entered} | Bob challenged: {challenge} | Success: {success}")
    return success

# Run once with honest prover
ali_baba_once(knows_password=True)

# Run once with malicious prover
ali_baba_once(knows_password=False)
