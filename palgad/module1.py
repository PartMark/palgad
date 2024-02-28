#Palgad
#def andmete_lisamine(i:list,p:list)->any:
#    """
#    """
#    while True:
#        try:
#            n=int(input("Mitu inimest"))
#            if n>0: break
#        except:
#            print("Viga. Proovi uuesti!")
#    for j in range(n):
#        nimi=input("Nimi: ")
#        palk=int(input("Palk: "))
#        i.append(nimi)
#        p.append(palk)
#    return i,p
#def naita_andmed(i:list,p:list):
#    """
#    """
#    for j in range(len(i)):
#        print(i[j],"-",p[j])
#def andmete_kustutamine(i:list,p:list)->any:
#    """
#    """
#    nimi=input("Keda kustutada ära?(nimi) ")
#    if nimi not in i:
#        print(f"{nimi} puudub")
#    else:
#        for j in range(len(i)):
#            if nimi in i:
#                p.pop(i.index(nimi))
#                i.remove(nimi)
#    return i,p
#def kellel_on_suurim_palk(i:list,p:list)->list:
#    """
#    """
#    nimed=[]
#    max_palk=max(p)
#    ind=p.index(max_palk)
#    for palk in p:
#        if max_palk==palk:
#            nimi=i[p.index(palk,ind)]
#            nimed.append(nimi)
#            ind+=1
#    return nimed
#def sorteerimine(i:list,p:list)->any:
#    """
#    """
#    for n in range(0,len(i)):
#        for m in range(n,len(i)):
#            if p[n]>p[m]:
#                p[n],p[m]=p[m],p[n]
#                i[n],i[m]=i[m],i[n]
#    return i,p

#Iseseisevtöö "Registreerimine ja autoriseerimine"

def registreerimine(nimed, paroolid):
    nimi = input("Sisesta kasutajanimi: ")
    if nimi in nimed:
        print("Kasutajanimi on juba võetud!")
        return
    valik = input("Kas soovite luua endale parooli (jah/ei)? ").lower()
    if valik == "jah":
        parool = input("Sisesta parool: ")
    else:
        parool = salasona(12)
        print("Teie automaatselt genereeritud parool on:", parool)
    nimed.append(nimi)
    paroolid.append(parool)
    print("Kasutaja registreeritud edukalt!")
import random
import string

def salasona(k: int):
    sala = ""
    for i in range(k):
        t = random.choice(string.ascii_letters)
        num = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        t_num = [t, str(num)]
        sala += random.choice(t_num)
    return sala
