def fibnum(n):
    listn = [0,1]
    i = 1
    while len(listn) < n:
        listn.append(listn[i] + listn[i-1])
        i += 1
        print(listn)
    return max(listn)
print(fibnum(5))