class Stack:
    def __init__(self) :
        self.items = []
        
    def push(self,value) :
        self.items.append(value)         

    def pop(self) :
        return self.items.pop()        

    def isEmpty(self) :
        return self.items == []

    def size(self) :
        return len(self.items)

def ManageStack(s,l1,l2) :
    if s[0] == 'A' :
        l1.push(s[1])
        print("Add =" , s[1])
    elif s[0] == 'P' :
        if l1.isEmpty() :
            print("-1")
        else:
            print("Pop =",l1.pop())
    elif s[0] == 'D' :
        if l1.isEmpty() :
            print("-1")
        else :
            for i in range(l1.size()-1,-1,-1) :
                if s[1] == l1.items[i] :
                   l2.push(l1.items[i])
            while not l2.isEmpty() :
                l1.items.remove(s[1])
                print("Delete = " + l2.pop())
    elif s[0] == 'LD' :
        if l1.isEmpty() :
            print("-1")
        else:
            for i in range(l1.size()-1,-1,-1) :
                if int(s[1]) > int(l1.items[i]) :
                    l2.push(l1.items[i])
            while not l2.isEmpty() :
                popInt = l2.items.pop(0)
                l1.items.remove(popInt)
                print("Delete = " + popInt + " Because " + popInt + " is less than " + s[1])
    elif s[0] == 'MD' :
        if l1.isEmpty() :
            print("-1")
        else :
            for i in range(l1.size()-1,-1,-1) :
                if int(s[1]) < int(l1.items[i]) :
                   l2.push(l1.items[i])
            while not l2.isEmpty() :
                popInt = l2.items.pop(0)
                l1.items.remove(popInt)
                print("Delete = " + popInt + " Because "+popInt+" is more than " + s[1])

l1 = Stack()
l2 = Stack()
inp = input ("Enter Input : ").split(",")
for e in inp :
    if len(e) > 1 :
        s = e.split()
    else :
        s = e
    ManageStack(s,l1,l2)
print("Value in Stack =",str(l1.items).replace("\'",""))
