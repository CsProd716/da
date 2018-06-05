def add(dic):
    k = str(input("Enter the phone "))
    v = float(input("Enter the price "))
    d1 = {k:v}
    dic.update(d1)
    return

def retrive(dic):
    s = str(input("Enter the phone"))
    print("The price of ",s,":", dic[s])
    return

def same(dic):
    new = {}
    for k,v in dic.iteritems():
        new.setdefault(v,[]).append(k)
    print(new)
        #print(v,"--->",k)
    return

def rem(dic):
    s = str(input("Give in the Phone"))
    if s in dic:
        del dic[s]
        print(s,"deleted from the dictionary")
    else:
        print("The phone not found in dictionary")
    return

def sort(dic):
    #print(sorted(dic.values()))
    print(sorted(dic,key = dic.__getitem__))
    return    

dic = {}

while(1):
    print("MENU")
    print("0.Show Dictionary")
    print("1.ADD a new entry")
    print("2.Search for info of one phone")
    print("3.Find phones with same price")
    print("4.Remove an entry")
    print("5.Display a price sorted list")
    print("9.EXIT")
    i = int(input("Choose the operation"))
    if i==0:
        print(dic.items())
    elif i==1:
        add(dic)
    elif i==2:
        retrive(dic) 
    elif i==3:
        same(dic)
    elif i==4:
        rem(dic)
    elif i==5:
       sort(dic)
    elif i==9:
        print("Exiting...\n")
        exit()
    

              
    
