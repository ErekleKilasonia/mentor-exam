def uniqpair(listn,n):
    pairs = []
    x = 0
    while x != len(listn):
        for i in range(len(listn)):
            if x != i:
                if listn[x] + listn[i] == n and (listn[x],listn[i]) not in pairs and (listn[i],listn[x]) not in pairs:
                    pairs.append((listn[x],listn[i]))
        x += 1
    return pairs
print(uniqpair([1, 2, 3, 2, 4],5))
print(uniqpair([1, 2, 3],7))
print(uniqpair([-1, 0, 1, 2, -2, 3],0))
                