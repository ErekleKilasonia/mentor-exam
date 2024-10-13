def majelement(listn):
    for i in listn:
        if listn.count(i) > len(listn)//2:
            return i
    
print(majelement([3, 2, 3]))
print(majelement([2, 2, 1, 1, 2]))
print(majelement([1, 1, 1, 1, 1]))