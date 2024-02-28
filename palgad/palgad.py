from module1 import *
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

while True:
    print("0-Andmed ekraanile\n1-Admete lisamine\n2-Andmete eemaldamine\n3-Kellel on suurim palk\n")
    vastus=int(input())
    if vastus==0:
        naita_andmed(inimesed,palgad)
    elif vastus==1:
        inimesed,palgad=andmete_lisamine(inimesed,palgad)
    elif vastus==2:
        inimesed,palgad=andmete_kustutamine(inimesed,palgad)
    elif vastus==3:
        rikkad_inimesed=kellel_on_suurim_palk(inimesed,palgad)
        print(rikkad_inimesed)
