import logic
def switch(scelta):
    scelta = int(scelta)
    if(scelta == 1):
        print("hai scelto l'inserimento di una nuova azione")
        return scelta
    elif(scelta == 2):
        print("hai scelto la stampa della lista")
        return scelta
    elif(scelta == 3):
        print("hai scelto l'eliminazione di un elemento dall lista")
        return scelta
    elif(scelta == 4):
        print("Uscita dal programma")
        return scelta
        