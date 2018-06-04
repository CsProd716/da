print("Input:")
line = []
while(1):
    l = input()
    line.append(l)
    if l == "Quit":
        break
rev = []
for i in range(2,len(line)+1):
    rev.append(line[len(line)-i])
for item in rev:
    print(item,end = " ")


