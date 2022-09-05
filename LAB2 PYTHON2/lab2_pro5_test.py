class TorKham:
    def __init__(self,kham) :
        self.kham = kham

    def Tor_kham(self) :
        list_word = []
        for num in self.kham :
            list_first = []
            list_first.append(str(num).split())
            if len(list_first[0]) == 2 :
                if 'P' in list_first[0] :
                    if len(list_word) > 0 and list_first[0][1].lower() in [word.lower() for word in list_word] :
                        pass
                    elif len(list_word) > 0 and list_word[-1][-2:].lower() != list_first[0][1][:2].lower() :
                        print("'" + list_first[0][1] + "'" + " -> ", end="")
                        print("game over")
                        break
                    else:
                        list_word.append(list_first[0][1])
                    print("'" + list_first[0][1] + "'" + " -> ", end="")
                    print(list_word)
                else:
                    print(f"'{list_first[0][0]} {list_first[0][1]}'"" is Invalid Input !!!")
                    break
            else:
                if 'R' in list_first[0] :
                    print("game restarted")
                    list_word = []

print("*** TorKham HanSaa ***")
kham = input("Enter Input : ").split(",")
TorKham = TorKham(kham).Tor_kham()