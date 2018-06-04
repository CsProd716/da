print("Input:")
line = []
while(1):
    l = input()
    if l.lower() == "quit":
        break
    line.append(l)
rev = []
for i in range(1,len(line)+1):
    rev.append(line[len(line)-i])
for item in rev:
    print(item,end = " ")


