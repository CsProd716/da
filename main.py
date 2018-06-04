from Sample import stack
print("Empty stack")
print(stack.GetStack())
while(1):
	print("1.Push\n2.Pop\n3.isEmpty\n4.Top")

	n = int(input("enter choice"))
	if n==1:
		item = int(input("Enter"))
		stack.Push(item)
	elif n==2:
		print(stack.Pop())
	elif n==3:
		print(stack.isEmpty())
	elif n==4:
		print(stack.Top())
	else:
		break
