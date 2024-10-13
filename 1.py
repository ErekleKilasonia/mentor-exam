def findnum(listn):
    listn = sorted(listn)
    mis_num = 1
    for i in range(1,len(listn)-1):
        if listn[i] + 1 != listn[i+1]:
            mis_num = listn[i] + 1
    if mis_num == 1:
        return listn[-1] + 1
    return mis_num
print(findnum([1, 2, 4, 5]))
print(findnum([1]))
print(findnum([2, 3, 1, 5]))

