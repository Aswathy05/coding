MOD = 10**9 + 7

def mod_inverse(n, mod):
    return pow(n, -1, mod)

def calculate_probability(N, b, w, x):
    total_outcomes = 6
    p_out = 1 / total_outcomes
    p_run = 1 / total_outcomes
    
    # Probability of getting out
    probability = p_out
    
    # Probability of scoring 1, 2, 3, 4, or 6 runs
    for run in [1, 2, 3, 4, 6]:
        if x + run >= N:
            # Kohli scores a century
            probability += p_run
    
    # Multiply by the multiplicative inverse of total outcomes modulo MOD
    result = int(probability * mod_inverse(total_outcomes, MOD)) % MOD
    return result

def main():
    T = int(input())
    for _ in range(T):
        N, b, w, x = map(int, input().split())
        result = calculate_probability(N, b, w, x)
        print(result)

if __name__ == "__main__":
    main()
