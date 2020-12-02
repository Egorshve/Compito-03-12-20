listacittà=[]
listatempmassima=[]
listatempminima=[]
escursionetermica=int(input("A quanto corrisponde l'escursione termica"))
contatore=0
while True:
    città=input("NOME CITTA':  ")
    listacittà.append(città)
    tempmassima=int(input("TEMPERATURA MASSIMA REGISTRATA:  "))
    listatempmassima.append(tempmassima)
    tempminima=int(input("TEMPERATURA MINIMA REGISTRATA:  "))
    differenzatemp=tempmassima-tempminima
    if differenzatemp>escursionetermica:
        contatore+=1
    continuo=int(input("Continuare?(1),Fine(2)"))
    if continuo==2:
        break
print("Le città che hanno superato il valore dell'escursione termica stabilito sono",contatore)
       
