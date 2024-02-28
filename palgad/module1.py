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
def andmete_kustutamine(i:list,p:list)->any:
    """
    """
    nimi=input("Keda kustutada ära?(nimi) ")
    if nimi not in i:
        print(f"{nimi} puudub")
    else:
        for j in range(len(i)):
            if nimi in i:
                p.pop(i.index(nimi))
                i.remove(nimi)
    return i,p
def kellel_on_suurim_palk(i:list,p:list)->list:
    """
    """
    nimed=[]
    max_palk=max(p)
    ind=p.index(max_palk)
    for palk in p:
        if max_palk==palk:
            nimi=i[p.index(palk,ind)]
            nimed.append(nimi)
            ind+=1
    return nimed
