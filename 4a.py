def initial():
    s = str(input("Give in the Full Name please..."))
    a = s.title()
    for i in range(len(a)):
       if a[i].isupper():
           print(a[i],end = ".")
       else:
           continue
initial()
