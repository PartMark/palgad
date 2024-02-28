from module1 import *
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

while True:
    print("0-Andmed ekraanile\n1-Admete lisamine\n")
    vastus=int(input())
    if vastus==0:
        naita_andmed(inimesed,palgad)
    elif vastus==1:
        inimesed,palgad=andmete_lisamine(inimesed,palgad)