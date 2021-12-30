import sys
import re

#ESERCIZIO: TROVA VOCALI
for line in sys.stdin:
    listamatch = re.findall(r"[aeiouAEIOU]", line)
    print(listamatch)
    print()
    print("Line: ", line)
    count = 0
    if not (listamatch == []):
        print("Trovate:")
        for match in listamatch:
            count = count + 1
            print(count, ":\t", match)
    else:
        print("Nessun match trovato")
       
#ESERCIZIO: PAROLA CHE INIZIA PER CONSONANTE
for line in sys.stdin:
    listamatch = re.findall(r"\b[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]\w+", line)
    print(listamatch)
    print()
    print("Line: ", line)
    if not (listamatch == []):
        print("Trovate:")
        for match in listamatch:
            print(match)
    else:
        print("Nessun match trovato")
#ESERCIZIO: PAROLA CHE TERMINA CON UN SEGNO DI PUNTEGGIATURA
for line in sys.stdin:
    listamatch = re.findall(r"\w+[,.;?!]\s", line)
    print(listamatch)
    print()
    print("Line: ", line)
    if not (listamatch == []):
        print("Trovate:")
        for match in listamatch:
            print(match)
    else:
        print("Nessun match trovato")
#ESERCIZIO: PAROLA CHE INIZIANO PER 'TRA' O 'TR'
for line in sys.stdin:
    listamatch = re.findall(r"\b[tar|tr]\w+", line)
    print(listamatch)
    print()
    print("Line: ", line)
    if not (listamatch == []):
        print("Trovate:")
        for match in listamatch:
            print(match)
    else:
        print("Nessun match trovato")
#ESERCIZIO: PASSATO PROSSIMO MANGIARE
for line in sys.stdin:
    listamatch = re.findall(r"\b[ho|hai|ha|abbiamo|avete|hanno]+ mangiato", line)
    print(listamatch)
    print()
    print("Line: ", line)
    if not (listamatch == []):
        print("Trovate:")
        for match in listamatch:
            print(match)
    else:
        print("Nessun match trovato")
#ESERCIZIO: DATA CON GIORNI, MESI E ANNO
for line in sys.stdin:
    listamatch = re.findall(r"\d{2}[-/]\d{2}[-/]\d{4}", line)
    print(listamatch)
    print()
    print("Line: ", line)
    if not (listamatch == []):
        print("Trovate:")
        for match in listamatch:
            print(match)
    else:
        print("Nessun match trovato")
#ESERCIZIO: VERTICALIZZARE PAROLA
for frase in sys.stdin:
    nuovafrase = re.sub(r" ", "\n", frase)
    print(nuovafrase)

