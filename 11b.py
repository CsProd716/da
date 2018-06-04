def subsetSum(ls, target):    
    for i in range(len(ls)):
        for j in range(i):
            for k in range(j):
                if ls[i]+ls[j]+ls[k] == target:
                    return True ,ls[i],ls[j],ls[k]
    return False
print("Enter a list of numbers: ") 
ls = [int(x) for x in input().split()] 
print("Enter the target: ") 
target = int(input()) 
#ls.sort() 
print(subsetSum(ls, target))
