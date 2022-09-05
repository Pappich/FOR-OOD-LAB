class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

q = Queue()
inp = input("Enter Input : ").split(",")
dq = []
for e in inp :
    if len(e) > 1 :
        index,value = e.split()
        q.enqueue(value)
        print(q.size())
    elif q.isEmpty() :
        print("-1")
    else :
        list = q.dequeue()
        dq.append(list)
        print(list,end = " ")
        print("0")
if q.isEmpty() :
    print("Empty")
                
for i in q.items :           
    print(i,end=" ")
