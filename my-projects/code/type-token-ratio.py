import collections
from collections import Counter

discorsi = open("speeches.txt", mode = "r", encoding = "utf-8")
lettura = discorsi.read().lower()
parole = lettura.split()
parole.sort()


def frequenza_parole(parole):
    counts = Counter(parole)
    return counts

def frequenza_ordinata(lista):
    ordine = collections.Counter(lista).most_common()
    return ordine[:50]

tokens = len(parole)
type_words = len(set(parole))
type_token_ratio = type_words/tokens
print(type_token_ratio)
