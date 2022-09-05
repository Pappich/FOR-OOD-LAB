class Queue:
    def __init__(self,list = None) :
        if list == None:
            self.items = []
        else:
            self.items = list

    def isEmpty(self) :
        return self.items == []

    def enqueue(self, item) :
        self.items.append(item)

    def dequeue(self) :
        return self.items.pop(0)

    def size(self) :
        return len(self.items)
    
inp = input("Enter people and time : ").split(' ')
q_main = Queue(list(inp[0]))
q_num = Queue(inp[1])
q1 = Queue()
q2 = Queue()
i = 1
qc = 0
qc_q2 = 0
while i <= int(q_num.items) :
    if qc == 3 :
         q1.dequeue()
         qc = 0
    if qc_q2 == 2 :
        q2.dequeue()
        qc_q2 = 0
    if q_main.size() != 0 and q1.size() < 5 :
        q1.enqueue(q_main.dequeue())
    elif q1.size() >= 5 and q_main.size() != 0 :
        q2.enqueue(q_main.dequeue())
    if q1.size() != 0 :
        qc += 1
    if q2.size() != 0 :
        qc_q2 = qc_q2 + 1
    print(i, q_main.items, q1.items, q2.items)
    i = i + 1
    
