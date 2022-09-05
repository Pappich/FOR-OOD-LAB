class range() :
    def __init__(self,x,y = 0,z = 1) :
        if(y == 0 and z == 1) :
            self.start = float(y)
        else : 
            self.start = float(x)
        if(y == 0) :
            self.end = float(x)
        else :
            self.end = float(y)
        self.step = float(z)
        self.i = []
    
    def new_range(self) :
        start = self.start
        end = self.end
        step = self.step
        i = self.i
        while(start < end) :
            temp = start
            temp = round(temp,3)
            i.append(temp)
            start = start + step
        return i

    def __str__(self) -> str :
        return '{self.i}'.format(self =self)
                
print("*** New Range ***")
num = list(input("Enter Input : ").split())
if len(num) == 3 :
    a = num[0]
    b = num[1]
    c = num[2]
elif len(num) == 2 :
    a = num[0]
    b = num[1]
    c = 1
elif len(num) == 1 :
    a = num[0]
    b = 0
    c = 1
test_range = range(a,b,c)
range_x = test_range.new_range()
l = [float(i) for i in range_x]
print('(',end='')
print(*l,sep=', ',end='')
print(')',end='')
