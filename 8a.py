def is_abecedarian(word):
    for i in range(0,len(word)-1):
        if (word[i]<word[i+1]) or (word[i]==word[i+1]):
            continue
        else:
            return False
    return True

s = str(input("Enter a word"))
print(is_abecedarian(s))
#count = 0 
#f = str(input("Enter the file name"))
#with open(f,"r") as file:
 #   for line in file:
  #      word = line.strip()
   #     if is_abecedarian(word):
    #        count +=1
    #print("There are {} abecedarian words".format(count))
