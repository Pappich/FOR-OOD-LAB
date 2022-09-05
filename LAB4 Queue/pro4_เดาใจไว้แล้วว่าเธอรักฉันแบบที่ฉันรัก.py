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

Act = { 0 : "Eat",1 : "Game",2 : "Learn",3 : "Movie"}
location = {0 : "Res.", 1 : "ClassR.", 2 : "SuperM.", 3 : "Home"}

inp = input("Enter Input : ").split(",")
myQ = Queue()
yourQ = Queue()
myAct = Queue()
yourAct = Queue()
myPlace = Queue()
yourPlace = Queue()

count = 0
count1 = 0
count2 = 0
count3 = 0

for i in range(len(inp)):
    x = inp[i].split(" ")
    myQ.enqueue(x[0])
    yourQ.enqueue(x[1])
    myActivity = Act[int(myQ.items[i][0])]
    myAct.enqueue(myActivity )
    yourActivity = Act[int(yourQ.items[i][0])]
    yourAct.enqueue(yourActivity)
    myLocation = location[int(myQ.items[i][2])]
    myPlace.enqueue(myLocation)
    yourLocation = location[int(yourQ.items[i][2])]
    yourPlace.enqueue(yourLocation)
    if myActivity == yourActivity and myLocation != yourLocation :
        count = count + 1
    elif myActivity != yourActivity and myLocation == yourLocation :
        count1 = count1 + 2
    elif myActivity == yourActivity and myLocation == yourLocation :
        count2 = count2 + 4
    elif myActivity != yourActivity and myLocation != yourLocation :
        count3 = count3 - 5
    num = count + count1 + count2 + count3
    
print('My   Queue = %s'%', '.join(map(str,myQ.items)))
print('Your Queue = %s'%', '.join(map(str,yourQ.items)))
print(f'My   Activity:Location = ',end="")
for i in range(myAct.size()) :
    if i != myAct.size()-1 :
        print(f"{myAct.items[i]}:{myPlace.items[i]}",end=", ")
    else :
        print(f"{myAct.items[i]}:{myPlace.items[i]} ")
print(f'Your Activity:Location = ',end="")
for j in range(yourAct.size()) :
    if j != yourAct.size()-1 :
        print(f'{yourAct.items[j]}:{yourPlace.items[j]}',end=", ")
    else :
        print(f'{yourAct.items[j]}:{yourPlace.items[j]} ')
if num >= 7 :
    print(f"Yes! You're my love! : Score is {num}.")
elif 0 < num < 7 :
    print(f"Umm.. It's complicated relationship! : Score is {num}.")
elif num < 0 :
    print(f"No! We're just friends. : Score is {num}.")
