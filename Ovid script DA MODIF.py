# -*- coding: utf-8 -*-
# Ovid Met. III Voglio contare tutti i nomi di divinità che ricorrono 
# con una funzione che sia riusabile per altre porzioni di testo
import re
def trova_conta (file, lista):
    dizionario = {}
    with open (file, 'r')as latin:
        text = latin.read()
        words = text.split()
        for lemmas in words:         
            if lemmas in lista:
                if lemmas in dizionario:
                    dizionario[lemmas] += 1
                else:
                    dizionario[lemmas] = 1
    return dizionario

        
def reg(testo, output):
    with open (testo, 'r') as latin:
        letto = latin.read()
        testo_modif = re.sub(r'\n', '/',letto)
    with open(output,'w') as new:
        new.write(testo_modif)

Ovid = r"C:\Users\giuli\Desktop\DATI\Python\Ovid Met III.txt"
divinità = ['Iuppiter', 'Iovem', 'Iuno', 'Iunone', 'Bacchus', 'Minerva']
nuovo_testo= r"C:\Users\giuli\Desktop\DATI\Python\Ovid Met III_allineato.txt"

risultati = trova_conta (Ovid, divinità)
print (risultati)

reg(Ovid, nuovo_testo)


        
        
        
        