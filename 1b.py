def stats(s):
    i = 0
    w = 0
    c = 0
    with open(s,"r") as file:
        for line in file:
            i+=1
            for character in line:
               if character in [" ","\n"]:
                   c=c
               else:    
                   c+=1
        file.seek(0)
        for word in file.read().split():
            w+=1
        file.close()
        
    print("Line Count:",i)
    print("Word Count:",w)
    print("Character Count:",c)
    return

p = str(input("Enter the File Name: "))
stats(p)
