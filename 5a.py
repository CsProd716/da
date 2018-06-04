def vowelcount():
    s = str(input("Give in the String"))
    l = {'a':0,'e':0,'i':0,'o':0,'u':0}
    for i in s:
        if i in ['a','A']:
            l['a']+=1
        elif i in ['e','E']:
            l['e']+=1
        elif i in ['i','I']:
            l['i']+=1
        elif i in ['o','O']:
            l['o']+=1
        elif i in ['u','U']:
            l['u']+=1
        else:
            continue
    print(l)
    return
vowelcount()
            
