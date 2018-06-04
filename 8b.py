class QueueFullError(Exception):
    pass
class QueueEmptyError(Exception):
    pass
class MyQueue:
    def __init__(self,size):
        self.size = size
        self.queue = []
    def Insert(self,element):
        if len(self.queue)>self.size:
            raise QueueFullError
        self.queue.append(element)
    def Delete(self):
        if self.queue == []:
            raise QueueEmptyError
        a = self.queue[0]
        del self.queue[0]
        return a
    def Display(self):
        if self.queue == []:
            raise QueueEmptyError
        print(self.queue)

try:
    n = int(input("Enter queue size"))
    q = MyQueue(n)
    while(1):
        choice = int(input("Choose from below:\n1.Insert\n2.Delete\n3.Display\n4.EXIT\n"))
        if choice == 1:
            e = int(input("Enter the element"))
            q.Insert(e)
        elif choice == 2:
            print(q.Delete(),"Deleted")
        elif choice == 3:
            q.Display()
        elif choice == 4:
            exit()
        else:
            print("Wrong choice entered")
            continue
except QueueFullError:
    print("Queue is full,cannot enter more elements")
except QueueEmptyError:
    print("Queue is empty,cannot perform the function")
      
