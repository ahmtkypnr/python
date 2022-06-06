def cumulative_sum(t):
    res = []
    x = 0
    for i in t:
        x += i
        res.append(x)
    return res

print(cumulative_sum([13,2,4,5]))
