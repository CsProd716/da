def is_abecedarian(word):
    for i in range(0,len(word)-1):
        if (word[i]>word[i+1]):
            return False       
    return True

#s = str(input("Enter a word"))
#print(is_abecedarian(s))
f = str(input("Enter the file name"))
with open(f,"r+") as file:
    count = 0 
    for line in file:
        for word in line.split():
            if is_abecedarian(word):
                count +=1
    print("There are {} abecedarian words".format(count))
file.close()
