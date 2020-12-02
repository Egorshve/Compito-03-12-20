import math
numerobinario=int(input("Inserire il numero binario:  "))
lunghezza=int(input("Da quante cifre è composto il numero binario?"))
contatorecifre=lunghezza
numerodecimale=0
esponente=0
while contatorecifre!=0:
    print("Qual'è la cifra in posizione",contatorecifre)
    cifra=int(input())
    fattore=math.pow(2,esponente)
    aggiunta=cifra*fattore
    numerodecimale+=aggiunta
    contatorecifre-=1
    esponente+=1
print("Il corrispondente numero decimale decimale di",numerobinario,"è",numerodecimale)
    