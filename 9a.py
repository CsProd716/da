def bubble(l):
    n = len(l)
    for i in range(n):
        for j in range(0,n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l

x = bubble([int(x) for x in input().split()])
print("Sorted list:")
print(x)


