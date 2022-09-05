numbers = input("Enter Your List : ")
if len(numbers.split()) < 3:
    print("Array Input Length Must More Than 2")
else:
    num_split = numbers.split()
    
def sum() :
    sumlist = []
    firstlist = []
    for x in range(len(num_split)):
        for y in range(x+1, len(num_split)):
            for z in range(y+1, len(num_split)):
                if int(num_split[x]) + int(num_split[y]) + int(num_split[z]) == 5:
                    sumlist.append(int(num_split[x]))
                    sumlist.append(int(num_split[y]))
                    sumlist.append(int(num_split[z]))
                    if sumlist not in firstlist:
                        firstlist.append(sumlist)
                    else:
                        pass
                    sumlist = []
    new_list = []
    return 