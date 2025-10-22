def muunnos(g):
    return g * 3.785

while True:
    gallona = float(input("Anna gallonamäärä. Negativiinen määrä keskeyttää ohjelman. "))
    if gallona < 0:
        break
    print(f"{gallona} gallonaa on {muunnos(gallona)} litraa.")