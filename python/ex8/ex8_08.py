def extract_tuples(test_list, K):
    result = []
    for tup in test_list:
        flag = True
        for x in tup:
            if len(str(x)) != K:
                flag = False
                break
        if flag:
            result.append(tup)
    return result
    
test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )]
K = 2
print(extract_tuples(test_list, K))
test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (782, )]
K = 3
print(extract_tuples(test_list, K))