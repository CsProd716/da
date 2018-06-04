class student:
    count = 0
    #pycount = 0
    def __init__(self,name,usn,subject):
        self.name = name
        self.usn = usn
        self.subject = subject
        #if self.subject.lower == "python":
            #student.pycount+=1
        student.count+=1
studlist = []
while(1):
    i = str(input("Enteries done:"))
    if i.lower() == "yes":
        break
    print()
    name = input("Enter name:")
    usn = input("Enter usn:")
    subject = input("Enter subject:")
    print()
    r = student(name,usn,subject)
    studlist.append(r)
for i in studlist:
    if i.subject.lower() == "python":
        print(i.name,"has opted for Python")
print("Number of students in class:",student.count)
