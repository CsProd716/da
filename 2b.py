def censor(s):
    with open(s,"r") as file:
        content = file.readlines()
        file.close()
    with open("censored.txt","w") as f:
        for line in content:
            for word  in line.split():
                if len(word) == 4:
                    f.write("xxxx")
                else:
                    f.write(word)
                f.write(" ")
            f.write("\n")
        f.close()
    return

s = str(input("Enter the file name"))
censor(s)
