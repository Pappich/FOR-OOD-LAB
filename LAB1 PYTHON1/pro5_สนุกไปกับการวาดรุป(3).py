n = int(input("Enter Input : "))
a = 2*(n+2)
for y in range(a) :
    for x in range(a) :
        white = (n-y+1) <= x <= (n+1) or (n+2<x<a-1 and 0<y<n+1)
        black = (n+1) < x <= (3*n+5-y)
        if 0<x<n+1 and n+2<y<a-1 :
            print('+',end='')
        elif white :
            print('#',end='')
        elif black :
            print('+',end='')
        else :
            print('.',end='')
    print()
              
