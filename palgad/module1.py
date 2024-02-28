def andmete_lisamine(i:list,p:list)->any:
    """
    """
    while True:
        try:
            n=int(input("Mitu inimest"))
            if n>0: break
        except:
            print("Viga. Proovi uuesti!")
    for j in range(n):
        nimi=input("Nimi: ")
        palk=int(input("Palk: "))
        i.append(nimi)
        p.append(palk)
    return i,p
def naita_andmed(i:list,p:list):
    """
    """
    for j in range(len(i)):
        print(i[j],"-",p[j])