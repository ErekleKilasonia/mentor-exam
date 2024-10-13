def findprefix(listn):
    strng = ""
    x = 0
    while x < len(sorted(listn,key=len)[0]):
        lstn = []
        for i in listn:
            lstn.append(i[x])
        if len(set(lstn)) == 1:
            strng += lstn[0]
        x += 1
    return strng
print(findprefix(["flower", "flow", "flight"] ))
print(findprefix(["dog", "racecar", "car"]))
print(findprefix(["apple", "apple", "apple"]))
    