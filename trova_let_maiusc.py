# Nel testo dell'Eneide trovo lettere maiuscole

def trova_lettere_maiuscole(testo):
    lettere_maiuscole = []
    for carattere in testo:
        if carattere.isupper():
            lettere_maiuscole.append(carattere)
    return lettere_maiuscole

testo = """Est in conspectu Tenedos, notissima fama
insula, dives opum, Priami dum regna manebant;
nunc tantum sinus, et statio male fida carinis.
Huc se provecti deserto in litore condunt.
Nos abiisse rati, et vento petiisse Mycenas.
Ergo omnis longo solvit se Teucria luctu:
panduntur portae: iuvat ire, et Dorica castra
desertosque videre locos, litusque relictum.
Hic Dolopum manus, hic saevus tendebat Achilles:
classibus hic locus, hic acies certare solebant."""

print("Lettere maiuscole nel testo:")
print(trova_lettere_maiuscole(testo))