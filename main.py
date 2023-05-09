import Lottery
import os

Lotteriet = Lottery.Lotteri()

looping = True

while looping:

    print("i loop")
    os.system("cls" if os.name == "nt" else "clear")
    antal_lotter =input("hur många lotter vill du ha max3!: ")
   
    try:
        int_antal_lotter = int(antal_lotter)
        i = 0

        if (int_antal_lotter <4):
            os.system("cls" if os.name =="nt" else "clear")
            print("Grattis du vann det här!")

            while i<int_antal_lotter:
                vinst = Lotteriet.get_vinst()
                print(vinst)
                i = 1+i

        elif(int_antal_lotter > 3):
            print ("to many rice bowl")
    except ValueError:
        print("error")

    print("------------------------------------------------------")
    spela_igen = input("vill du spela igen? ")

    if (spela_igen=="n"):
        break