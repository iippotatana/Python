#4 Usare un ciclo for per stampare su terminale (print) 
#le coppie chiave:valore  del dizionario del punto precedente

dizionario = {"a":["carta", "forbice", "sasso"],"b":("cuori", "picche", "fiori", "quadri"),"c":{"gennaio", "febbraio", "marzo"},"d":{"d1": (1, 2, 3), "d2":[4, 5, 6], "d3":{7, 8, 9}}}

for chiave,valore in dizionario.items():
    print(f"Chiave:{chiave}  Valore: {valore}")
    