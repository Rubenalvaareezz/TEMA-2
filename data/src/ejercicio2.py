def extrae_numero(texto):
    palabras = texto.split()
    res=[]
    for p in palabras:
        if p.isdigit():
            res.append(int(p))

    return res

if __name__ == "__main__":
    print(extrae_numero("Mi amigo me debe 80 euros de 4 entradas del cine"))
    
