numerodecimale=int(input("Numero decimale da trasformare in binario:  "))
numerobinario=[]
quoziente=int(numerodecimale/2)
valore=0
if quoziente==0:
    valore+=1
resto=int(numerodecimale%2)
numerobinario.append(resto)
while True and valore!=1:
    quoziente=int(quoziente/2)
    if quoziente==0:
        break
    resto=int(quoziente%2)
    numerobinario.append(resto)
print("Il numero binario corrispondente è:   ")
for n in reversed(numerobinario):
    print(n)