class Stack :
    def __init__(self,list = None) :
        if list == None :
            self.items = []
        else :
            self.items = list

    def push(self,i) :
        self.items.append(i)

    def pop(self) :
        return self.items.pop()

    def isEmpty(self) :
        return self.items == []

    def size(self) :
        return len(self.items)
    
    def peek(self) :
        return self.items[-1]

class Queue :
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

    def size(self) :
        return len(self.items)
    
    def peek(self) :
        return self.items[-1]

inp = input("Enter Input (Normal, Mirror) : ").split()
normal = Queue()
mirror = Stack()
NormalBoom = 0
NormalBoomFailed = 0
mirrorQueue = Queue()
mirrorBoom = 0
for i in reversed(inp[1]) :
    mirror.push(i)
    if (mirror.size() >= 3) and ((mirror.items[-1] == mirror.items[-2] == mirror.items[-3])) :
        mirrorQueue.enqueue(mirror.pop())
        mirror.pop()
        mirror.pop()
        mirrorBoom = mirrorBoom + 1
        
for i in inp[0] :
    normal.enqueue(i)
    if (normal.size() >= 3) and (normal.items[-1] == normal.items[-2] == normal.items[-3]) and not mirrorQueue.isEmpty() :
        temp_pop = normal.items.pop()
        normal.enqueue(mirrorQueue.dequeue())
        normal.enqueue(temp_pop)
        if (normal.items[-1] == normal.items[-2] == normal.items[-3]) :
            normal.items.pop()
            normal.items.pop()
            normal.items.pop()
            NormalBoomFailed = NormalBoomFailed + 1
    else:
        if (normal.size() >= 3) and (normal.items[-1] == normal.items[-2] == normal.items[-3]) :
            normal.items.pop()
            normal.items.pop()
            normal.items.pop()
            NormalBoom = NormalBoom + 1

print("NORMAL :")
print(normal.size())
if normal.size() == 0 :
    print('Empty')
else :
    print(''.join(reversed(normal.items)))
print(f'{NormalBoom} Explosive(s) ! ! ! (NORMAL)')
if NormalBoomFailed != 0 :
    print(f'Failed Interrupted {NormalBoomFailed} Bomb(s)')

print('------------MIRROR------------')
print(': RORRIM')
print(mirror.size())
if mirror.size() == 0 :
    print("ytpmE")
else :
    print(''.join(reversed(mirror.items)))
print(f'(RORRIM) ! ! ! (s)evisolpxE {mirrorBoom}')
