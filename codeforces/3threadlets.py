
t = int(input())
for i in range(t):
    a, b, c = (int(i) for i in input().split())
     # Sort the threadlet lengths in ascending order
    lengths = sorted([a, b, c])
    
    # Check if it's possible to make all threadlets of equal length in at most three moves
    if lengths[0] + lengths[1] + 1 >= lengths[2]:
        print("YES")
    else:
        print("NO")
