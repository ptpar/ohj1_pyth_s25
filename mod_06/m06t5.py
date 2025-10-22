def parilliset(l):
    uusi = []
    for i in l:
        if i % 2 == 0:
            uusi.append(i)
    return uusi

lista = [1,2,3,4]
print("Alkuperäinen lista:", lista)
print("Karsittu lista:", parilliset(lista))