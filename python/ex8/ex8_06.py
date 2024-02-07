def frequency_list(input_list):
    frequency = []
    for item in input_list:
        found = False
        for i in range(len(frequency)):
            if item == frequency[i][0]:
                frequency[i][1] += 1
                found = True
                break
        if not found:
            frequency.append([item, 1])
    return [(key, value) for key, value in frequency]
    
input_list = eval(input("enter the list:"))
print("Input List :", input_list)
print("List of tuples :", frequency_list(input_list))