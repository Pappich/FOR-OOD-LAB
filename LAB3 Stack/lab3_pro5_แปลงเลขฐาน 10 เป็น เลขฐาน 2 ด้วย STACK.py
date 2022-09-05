class Stack :
    total = 0
    def __init__(self) :
        self.token = []
        self.size = 0

    def push(self, token) :
        return self.token.append(token)
        
    def pop(self) :
        return self.token.pop()
    
    def isEmpty(self) :
        return self.token == []

    def dec2bin(token) :
        s = Stack()
        while token > 0 :
            remainder = token % 2
            s.push(remainder)
            token = token // 2
        binary_number = ""
        while not s.isEmpty() :
            binary_number = binary_number + str(s.pop())
        return binary_number

print(" ***Decimal to Binary use Stack***")
token = int(input("Enter decimal number : "))
print("Binary number : ",end='')
print(Stack.dec2bin(int(token)))
