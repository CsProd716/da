items = []
def GetStack():
	return items
def isEmpty():
	if items == []:
		return True
	else:
		return False
def Top():
	return items[len(items)-1]
def Push(item):
	items.append(item)
def Pop():
	return items.pop()

