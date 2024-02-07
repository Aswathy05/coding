MOD = 10**9 + 7

def count_beautiful_strings(N, S):
    # Calculate the frequency of each character in S
    char_freq = [0] * 26
    for char in S:
        char_freq[ord(char) - ord('a')] += 1
    
    # Calculate the factorial of a number modulo MOD
    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result = (result * i) % MOD
        return result
    
    # Calculate the inverse factorial of a number modulo MOD
    def inv_factorial(n):
        result = 1
        for i in range(1, n + 1):
            result = (result * pow(i, MOD - 2, MOD)) % MOD
        return result
    
    # Calculate the number of unique beautiful strings using the formula
    ans = factorial(N)
    for freq in char_freq:
        ans = (ans * inv_factorial(freq)) % MOD
    
    return ans

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().strip()
        result = count_beautiful_strings(N, S)
        print(result)

if __name__ == "__main__":
    main()
