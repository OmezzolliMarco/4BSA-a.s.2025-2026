def trovaPrefisso(a:str, b:str):
    lunghezza = min(len(a), len(b))
    prefisso = ""
    for i in range(lunghezza):
        if a[i]==b[i]:
            prefisso += a[i]
        else:
            return prefisso

def trovaSuffisso(a:str, b:str):
    suffisso = trovaPrefisso(a[::-1], b[::-1])
    return suffisso[::-1]


a = input("Inserisci una parola: ")
b = input("Inserisci una parola: ")

print(trovaPrefisso(a,b))
print(trovaSuffisso(a,b))