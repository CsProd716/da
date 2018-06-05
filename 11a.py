dic = {}
def add():
    word = str(input("Enter the word "))
    mean = str(input("Enter the meaning "))
    d1 = {word:mean}
    dic.update(d1)
    return
def retrive():
    w = str(input("Enter the word"))
    print("The meaning of ",w,":", dic[w])
    return
def search():
    w = str(input("Enter the word"))
    if w in dic:
        print("Found")
    else:
        print("There is no word like that in the dictionary")
def same():
    m = str(input("Enter the meaning "))
    for word,mean in dic.items():
        if mean == m:
            print(word,end = " ")
    print()        
def rem():
    word = str(input("Enter the word "))
    del dic[word]
def sortdisplay():
    print(sorted(dic))


while(1):
    print("MENU")
    print("0.Show Dictionary")
    print("1.ADD a new entry")
    print("2.Retrive meaning")
    print("3.same meaning words")
    print("4.Remove an entry")
    print("5.Display a word sorted list")
    print("6.Search for a word")
    print("9.EXIT")
    i = int(input("Choose the operation"))
    if i==0:
        print(dic.items())
    elif i==1:
        add()
    elif i==2:
        retrive() 
    elif i==3:
        same()
    elif i==4:
        rem()
    elif i==5:
        sortdisplay()
    elif i==6:
        search()
    elif i==9:
        print("Exiting...\n")
        exit()
