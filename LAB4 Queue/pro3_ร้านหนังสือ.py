class Queue:
    def __init__(self,list = None) :
        if list == None : 
            self.items = []
        else :
            self.items = list

    def enqueue(self,i) :
        self.items.append(i)
        
    def dequeue(self) :
        return self.items.pop(0)
    
    def isEmpty(self) :
        return self.items == []  
    
inp = input("Enter Input : ").split("/")
book = inp[0]
value = inp[1]
a = value.split(",")
q = Queue(book.split())
for e in a :
    addValue = e.split()
    if addValue[0] == 'D' :
        q.dequeue()
    elif addValue[0] == 'E' :
        q.enqueue(addValue[1])       
bookshelf = []
Duplicate = False
for i in q.items :
    if i in bookshelf :
        print("Duplicate")
        Duplicate = True
        break  
    else :
        bookshelf.append(i)
if Duplicate == False :
    print("NO Duplicate")
            
