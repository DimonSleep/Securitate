# Criptarea Rishelieu
def construieste_cheie_rishelieu(n):
    cheie_rishelieu = [[0] * n for _ in range(n)]
    litera = ord('A')
    
    for i in range(n):
        for j in range(n):
            cheie_rishelieu[i][j] = chr(litera)
            litera += 1
    
    return cheie_rishelieu

def criptare_rishelieu(text, cheie):
    n = len(cheie)
    text_criptat_rishelieu = ""

    for i in range(0, len(text), n):
        bloc_text = text[i:i+n]

        for rotatie in range(3):
            cheie = [list(row) for row in zip(*cheie[::-1])]

        for i in range(n):
            for j in range(n):
                if cheie[i][j] == "1":
                    text_criptat_rishelieu += bloc_text[j * n + i]

    return text_criptat_rishelieu

# Citirea textului clar dintr-un fișier
with open("ALFABET1.TXT", 'r') as f:
    text_clar_rishelieu = f.read().strip()

# Construirea cheii Rishelieu
cheie_rishelieu = construieste_cheie_rishelieu(4)

# Aplicarea criptării Rishelieu
text_criptat_rishelieu = criptare_rishelieu(text_clar_rishelieu, cheie_rishelieu)

# Afișarea rezultatului
print("Text criptat Rishelieu:", text_criptat_rishelieu)

# Afișarea cheii Rishelieu
print("Cheie Rishelieu:")
for row in cheie_rishelieu:
    print(row)

# Afișarea blocurilor de text
print("Blocuri de text:")
for i in range(0, len(text_clar_rishelieu), len(cheie_rishelieu)):
    print(text_clar_rishelieu[i:i+len(cheie_rishelieu)])

# Aplicarea criptării Rishelieu
text_criptat_rishelieu = criptare_rishelieu(text_clar_rishelieu, cheie_rishelieu)

# Afișarea rezultatului
print("Text criptat Rishelieu:", text_criptat_rishelieu)

# Aplicarea criptării Rishelieu
text_criptat_rishelieu = criptare_rishelieu(text_clar_rishelieu, cheie_rishelieu)

# Afișarea rezultatului
print("Text criptat Rishelieu:", text_criptat_rishelieu)