def remove_tuples(test_list, K):
    return [tuple_item for tuple_item in test_list if len(tuple_item) !=K]
    
test_list = eval(input("Enter a list of tuples: "))
K = int(input("Enter the length of tuples to be removed: "))
print("Original List :", test_list)
print("List after removing tuples of length :", K)
print(remove_tuples(test_list, K))