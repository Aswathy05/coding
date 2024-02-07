def create_tuple_list(n):
    tuple_list = []
    for i in range(1, n+1):
        tuple_list.append((i, i**3))
    return tuple_list
n = int(input("Enter a positive integer: "))
result = create_tuple_list(n)
print("The list of tuples:", result)