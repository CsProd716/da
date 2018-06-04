def partition(ls):
  result=[]
  for name in ls:
    if name[0].lower() in 'abcdefghijklm':
      result.append(name)
  print(result)
ls = [str(x) for x in input("Enter first names please: ").split()]
partition(ls)
