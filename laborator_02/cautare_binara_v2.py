from array import array

lista=[]
poz=[]
numar_elemente=input("Numarul de elemente din lista: ")
numar_elemente=int(numar_elemente)
for i in range(0, int(numar_elemente)):
    print("introdu elementul V[",i,"] =", end="")
    elemente=input()
    lista.append(elemente)

print("lista=  ", lista)
lista.sort()


def cautare_binara(lista, element, numar_elemente):
    stanga=0
    dreapta=len(lista)-1

    while stanga<=dreapta:
        mijloc=(stanga+dreapta)//2
        if lista[mijloc]==element:
            return mijloc
           
        elif lista[mijloc]<element:
            stanga=mijloc+1
        else:
            dreapta=mijloc-1
    return -1

element=input("introdu numarul pe care vrei sa il cauti: ")

print("numarul cautat se afla pe pozitia: ", cautare_binara(lista, element, numar_elemente))
print("Numarul ", element, " apare de :", lista.count(element), " ori")
