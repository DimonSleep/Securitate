def creare_alfabet():
    print("Introdu fraza cheie:")
    fraza = input().upper()
    alfabet = set(fraza)
    
    with open("alfabet1.txt", 'w') as alfabet1:
        for c in alfabet:
            print(c, end='', file=alfabet1)

        with open("alfabet.txt", 'r') as alf:
            for c in alf.read():
                if c not in alfabet:
                    print(c, end='', file=alfabet1)

    return alfabet

def init(dim):
    print(f'Numarul de caractere in alfabet este de: {dim}')
    print("Introduceti numarul de linii si coloane a tabelului:")
    lin = int(input("Numarul de linii: "))
    col = int(input("Numarul de coloane: "))
    print("Ce caractere eliminati din alfabet?")
    print("Introduceti aceste caractere.")
    print("Finalizati introducerea caracterelor cu simbolul /")

    c_eliminate = set()
    while True:
        x = input()
        if x == '/':
            break
        c_eliminate.add(x)

    alfabet = []
    with open("alfabet1.txt", 'r') as alfabet1:
        for i in range(lin):
            row = []
            for j in range(col):
                x = alfabet1.read(1)
                if x not in c_eliminate:
                    row.append(x)
                else:
                    x = alfabet1.read(1)
                    row.append(x)
            alfabet.append(row)

    for i in range(lin):
        for j in range(col):
            print(f"{alfabet[i][j]:3}", end='')
        print()

    return alfabet

def cript(dim, alfabet):
    with open("clar.txt", 'r') as f, open("cript.txt", 'w') as g:
        while True:
            x = f.read(1)
            if not x:
                break
            y = f.read(1)

            a1, b1, a2, b2 = 0, 0, 0, 0
            for a in range(len(alfabet)):
                for b in range(len(alfabet[0])):
                    if x == alfabet[a][b]:
                        a1, b1 = a, b
                    if y == alfabet[a][b]:
                        a2, b2 = a, b

            if a1 == a2:
                if b1 < b2:
                    b1 += 1
                    b2 += 1
                    if b2 == len(alfabet[0]):
                        b2 = 0
                elif b1 > b2:
                    b1 -= 1
                    b2 -= 1
                    if b2 == -1:
                        b2 = len(alfabet[0]) - 1
                else:
                    b2 -= 1
                    if b2 == -1:
                        b2 = len(alfabet[0]) - 1
                    b1 = b2
            elif b1 != b2:
                temp = b1
                b1 = b2
                b2 = temp

            if b1 == b2:
                if a1 < a2:
                    a1 += 1
                    a2 += 1
                    if a2 == len(alfabet):
                        a2 = 0
                elif a1 > a2:
                    a1 -= 1
                    a2 -= 1
                    if a2 == -1:
                        a2 = len(alfabet) - 1
                else:
                    a2 -= 1
                    if a2 == -1:
                        a2 = len(alfabet) - 1
                    a1 = a2

            print(a1, b1, a2, b2)
            print(alfabet[a1][b1], alfabet[a2][b2], file=g)

# Functia de decriptare nu este implementata pentru ca este necesar sa avem
# acces la cheie in timpul decriptarii

dim = creare_alfabet()
alfabet = init(dim)
cript(dim, alfabet)
