# Nel testo dell'Eneide voglio trovare i nomi propri, a prescindere
# che siano toponimi o nomi di persona

def trova_nomi_propri(testo):
    parole = testo.split()
    nomi_propri = []
    for parola in parole:
        if parola[0].isupper() or (parola[-1].isupper() and parola[-2:] not in [';', '.']):
            nomi_propri.append(parola)
    return nomi_propri

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

print("Nomi propri nel testo:")
print(trova_nomi_propri(testo))