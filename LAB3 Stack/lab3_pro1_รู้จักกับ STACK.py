def Create() :
    stack = []
    return stack

def push(stack,item) :
    stack.append(item)
    print(f"Add = {item} and Size = {len(stack)}")

def pop(stack) :
    if len(stack) == 0 :
        print("-1")
    else:
        return print(f"Pop = {stack.pop()} and Index = {len(stack)}")

def Valueindex(stack) :
    for x in stack :
        print(x,end=" ")

list = input("Enter Input : ").split(",")
s = Create()
for x in range(len(list)) :
    if len(list[x]) == 4 :
        if 'A' in list[x] :
            push(s, str(list[x][-2] + list[x][-1]))
    else:
        if 'P' in list[x] :
            pop(s)

if len(s) != 0 :
    print("Value in Stack = ", end="")
    Valueindex(s)
else:
    print("Value in Stack = Empty")
