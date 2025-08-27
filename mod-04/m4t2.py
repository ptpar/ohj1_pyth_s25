while True:
    tuumat = float(input("Anna tuumamäärä. Negatiivinen luku keskeyttää ohjelman. "))
    if tuumat < 0:
        break
    print("Tuumat senttimetreinä:", tuumat * 2.54)