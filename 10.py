def groupanagrams(listn):
    lstn = []
    x = 0
    while x != len(listn):
        lst = []
        for i in range(len(listn)):
            if sorted(listn[x]) == sorted(listn[i]):
                lst.append(listn[i])
        if sorted(lst) not in lstn:
            lstn.append(sorted(lst))
        x += 1
    return lstn
print(groupanagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupanagrams(["abc", "bac", "cab"]))
print(groupanagrams(["hello", "world", "python"]))

