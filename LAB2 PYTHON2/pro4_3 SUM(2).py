def CoutntNumber(num) :
    if len(num.split()) < 3 :
        print("Array Input Length Must More Than 2")
    else :
        num_split = num.split()
        sum_list = []
        first_list = []
        for x in range(len(num_split)) :
            for y in range(x+1,len(num_split)) :
                for z in range(y+1,len(num_split)) :
                    if int(num_split[x]) + int(num_split[y]) + int(num_split[z]) == 5 :
                        sum_list.append(int(num_split[x]))
                        sum_list.append(int(num_split[y]))
                        sum_list.append(int(num_split[z]))
                        if sum_list not in first_list :
                            first_list.append(sum_list)
                        else :
                            pass
                        sum_list = []
        new_list = []
        if len(first_list) > 2 :
            new_list.append(first_list[2])
            print(new_list)
        else:
            print(first_list)

numbers = input("Enter Your List : ")
CoutntNumber(numbers)
