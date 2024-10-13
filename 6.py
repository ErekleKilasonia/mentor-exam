def listsavg(list1,list2):
    listn = list1 + list2
    return sum(listn)/len(listn)
print(listsavg([1, 2, 3], [4, 5, 6]))
print(listsavg([10, 20], [30, 40, 50]))
print(listsavg([-5, -3, -1], [1, 3, 5]))