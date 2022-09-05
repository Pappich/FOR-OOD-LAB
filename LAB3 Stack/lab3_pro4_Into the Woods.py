class Stack :
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.items)
    
    def peek(self) :
        return self.items[-1]
    
S = Stack()
stack = []
inp = input('Enter Input : ').split(',')
for i in range(len(inp)) :
    if inp[i] == 'B' :
        a = 0
        count = 0
        for j in range(S.size()) :
            b = int(S.pop())
            if a < b :
                count = count + 1
                a = b
        print(count)
        for k in range(len(stack)) :
            S.push(stack[k])
    else :
        list = inp[i].split(' ')
        S.push(list[1])
        stack.append(list[1])
        
