Operators = set(['+', '-', '*', '/', '(', ')', '^']) 
Priority = {'(': 0,
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
            }
class Stack :    
    def __init__(self,list = None) :
        if list == None :
            self.items = []
        else:
            self.items = list
    
    def push(self, value) :
        self.items.append(value)
        
    def pop(self) :
        return self.items.pop()

    def size(self) :
        return len(self.items)

    def isEmpty(self) :
        return self.items == []
    
    def peek(self) :
        return self.items[-1]
    
inp = input('Enter Infix : ')
S = Stack()
print('Postfix : ', end='')
### Enter Your Code Here ###
for ch in inp :
    if ch not in Operators : 
        print(ch,end='')
    else :
        if ch == '(' :  
            S.push(ch)
        elif ch == ')' :
            while S.peek() != '(' :
                print(S.pop(),end='')
            S.pop()
        elif S.isEmpty() or Priority[ch] > Priority[S.peek()] :   
            S.push(ch) 
        else :
            while not S.isEmpty() and S.peek() != '(' and Priority[S.peek()] >= Priority[ch] :
                print(S.pop(),end='')
            S.push(ch) 
while not S.isEmpty() :
    print(S.pop(), end='')
print()  
     
