from switch import *
from logic import *

todo_list = []
selezione = 0
print("scegli un'azione da effettuare:")
print("1. inserisci nuova azione")
print("2. stampa todo")
print("3. elimina elemento dalla lista")
print("4. esci")
scelta = input("scegli un numero: ")
#print(f"hai scelto il numero {scelta}")
if(selezione == 1):
    print("inserisci un elemento nella Todo list:")
    elemento = input()
    gestione_inserimento(todo_list,elemento)
    gestione_stampa(todo_list)
elif(selezione == 2):
    gestione_stampa(todo_list)
elif(selezione == 3):
    gestione_stampa(todo_list)
elif(selezione == 4):
    exit(1)




