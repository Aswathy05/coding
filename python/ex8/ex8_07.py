def remove_duplicates(input_tuple):
    output_tuple = []
    for item in input_tuple:
        if item not in output_tuple:
            output_tuple.append(item)
    return tuple(output_tuple)
    
input_tuple = (1, 2, 3, 1, 2, 1, 2, 3, 4, 5, 4, 5, 4, 5)
print("Input Tuple :", input_tuple)
print("Tuple without duplicates :", remove_duplicates(input_tuple))