#from module1 import *
#palgad=[1200,2500,750,395,1200]
#inimesed=["A","B","C","D","E"]

#while True:
#    print("0-Andmed ekraanile\n1-Admete lisamine\n2-Andmete eemaldamine\n3-Kellel on suurim palk\n4-Sorteerime\n")
#    vastus=int(input())
#    if vastus==0:
#        naita_andmed(inimesed,palgad)
#    elif vastus==1:
#        inimesed,palgad=andmete_lisamine(inimesed,palgad)
#    elif vastus==2:
#        inimesed,palgad=andmete_kustutamine(inimesed,palgad)
#    elif vastus==3:
#        rikkad_inimesed=kellel_on_suurim_palk(inimesed,palgad)
#        print(rikkad_inimesed)
#    elif vastus==4:
#        inimesed,palgad=sorteerimine(inimesed,palgad)

#Iseseisevtöö "Registreerimine ja autoriseerimine"
from module1 import *
nimed=[]
paroolid=[]

while True:
    print("\nValige tegevus:")
    print("1. Registreerimine")
    print("2. Autoriseerimine")
    print("3. Nime või parooli muutmine")
    print("4. Unustasin parooli taastamine")
    print("5. Lõpetamine")

    vastus = input("Sisestage valiku number: ")

    if vastus==1:
        registreerimine(nimed, paroolid)
    elif vastus==2:
        nimi = input("Sisesta kasutajanimi: ")
        parool = input("Sisesta parool: ")
        if nimi in nimed:
            index = nimed.index(nimi)
            if parool == paroolid[index]:
                print("Autoriseerimine õnnestus!")
            else:
                print("Vale parool!")
        else:
            print("Kasutajat ei leitud!")
    elif vastus==3:
        pass
    elif vastus==4:
        pass
    elif vastus==5:
        print("Programm lõpetatakse.")
        break
    else:
        print("Vigane valik, palun valige uuesti.")
