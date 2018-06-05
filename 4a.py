def initial():
    s = str(input("Give in the Full Name please..."))
    for w in s.split():
        print(w[0].upper(),end = "")
    print()
initial()
