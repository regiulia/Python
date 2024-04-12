# Elenco delle tragedie di Eschilo ordinate anno per anno

tragedie_eschilo = {
    "458 a.C.": ["Agamennone", "Coefore", "Eumenidi"]
    "463 a.C.": 'Supplici'
    "460 a.C.": 'Prometeo'
    "472 a.C.": 'Persiani' 
    }

def elenca_tragedie_per_anno(tragedie_per_anno):
    for anno, tragedie in tragedie_per_anno.items():
        print(f"{anno}: {', '.join(tragedie)}")

print("Tragedie di Eschilo superstiti anno per anno:")
elenca_tragedie_per_anno(tragedie_eschilo)