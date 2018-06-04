try:
    print(1+'msrit')
except TypeError:
    print("Type Error occured")

try:
    L = [1,2,3]
    print(L[4])
except IndexError:
    print("Index overflow")
