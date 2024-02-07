import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
def calculate_votes(u, leaders, votes):
    # Initialize votes for employee u
    votes[u] = 1

    # Traverse the subordinates of employee u
    for v in leaders[u]:
        votes[u] += calculate_votes(v, leaders, votes)

    return votes[u]

def can_be_sole_winner(u, leaders, votes):
    # Check if employee u can be the sole winner
    for v in leaders[u]:
        if votes[u] <= votes[v]:
            return False
    return True

def find_sole_winner(N, P):
    # Create a list to store leaders for each employee
    leaders = [[] for _ in range(N + 1)]

    # Populate the leaders list
    for u in range(2, N + 1):
        leaders[P[u - 2]].append(u)

    # Initialize votes array
    votes = [0] * (N + 1)

    # Calculate votes for each employee starting from the CEO
    calculate_votes(1, leaders, votes)

    # Find employees who can be the sole winner
    sole_winners = [1 if can_be_sole_winner(u, leaders, votes) else 0 for u in range(1, N + 1)]

    return "".join(map(str, sole_winners))

# Input reading and testcase processing
T = int(input("Enter the number of testcases: "))
for _ in range(T):
    N = int(input())
    P = list(map(int, input().split()))

    result = find_sole_winner(N, P)
    print(result)
