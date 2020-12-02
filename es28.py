studenti=[]
lanci=[]
aggiunta=0
while True:
    aggiunta=int(input("LANCIO DELLO STUDENTE:  "))
    lanci.append(aggiunta)
    if aggiunta==1:
        break
    aggiunta=input("NOME STUDENTE:  ")
    studenti.append(aggiunta)
listafinale=zip(lanci,studenti)
print(list(listafinale))
lanciosuper=max(lanci)
print("Il lancio migliore è stato",lanciosuper,"m")