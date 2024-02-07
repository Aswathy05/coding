def dfs(v, parent, graph, positions):
    for u in graph[v]:
        if u != parent:
            positions[u].add(positions[v].pop())
            dfs(u, v, graph, positions)

def find_winner(N, positions, graph):
    dfs(1, -1, graph, positions)

    for i in range(3):
        if positions[i] & positions[(i + 1) % 3]:
            return chr(ord('A') + i)
    
    return "DRAW"

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        positions = [set(map(int, input().split())) for _ in range(3)]
        graph = {i: [] for i in range(1, N + 1)}

        for _ in range(N - 1):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        winner = find_winner(N, positions, graph)
        print(winner)

if __name__ == "__main__":
    main()
