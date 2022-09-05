class gameTorKham :
    def __init__(self,kham) :
        self.kham = kham

    def Tor_kham(self) :
        word_list = []
        for num in self.kham :
            first_list = []
            first_list.append(str(num).split())
            if len(first_list[0]) == 2 :
                if 'P' in first_list[0] :
                    if len(word_list) > 0 and first_list[0][1].lower() in [word.lower() for word in word_list] :
                        pass
                    elif len(word_list) > 0 and  first_list[0][1][:2].lower() != word_list[-1][-2:].lower() :
                        print("'" + first_list[0][1] + "'" + " -> ", end = "")
                        print("game over")
                        break
                    else:
                        word_list.append(first_list[0][1])
                    print("'" + first_list[0][1] + "'" + " -> ", end = "")
                    print(word_list)
                else:
                    print(f"'{first_list[0][0]} {first_list[0][1]}'"" is Invalid Input !!!")
                    break
            else:
                if 'R' in first_list[0]:
                    print("game restarted")
                    word_list = []

print("*** TorKham HanSaa ***")
kham = input("Enter Input : ").split(",")
TorKham = gameTorKham(kham).Tor_kham()