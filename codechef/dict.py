dict={1:50,2:49,3:48}
minClan = min(dict, key=dict.get)
minDays = min(dict.values(), key=lambda x: x)
print(minClan,minDays)