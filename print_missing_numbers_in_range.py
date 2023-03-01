# print missing number between range

start,end = 1,10000
lst = range(500,50000)
complete_numset = set(range(start,end+1))
in_range_set = set(filter(lambda num: num in complete_numset, lst))
print(complete_numset.difference(in_range_set))




