    def can_rearrange_arrays(t, test_cases):
        results = []

        for _ in range(t):
            n = test_cases[_][0]
            a = test_cases[_][1]
            b = test_cases[_][2]

            # Sort array A in non-decreasing order
            a.sort()

            # Check if A[i] is less than or equal to B[i] for all i
            possible = all(a[i] != a[i+1] and a[i] <= b[i] for i in range(n-1))

            if possible:
                results.append("YES")
            else:
                results.append("NO")

        return results

    # Input
    t = int(input())
    test_cases = []

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        test_cases.append((n, a, b))

    # Output
    results = can_rearrange_arrays(t, test_cases)

    for result in results:
        print(result)
