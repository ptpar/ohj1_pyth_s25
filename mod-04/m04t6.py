# toistot N = pisteiden kokonaismäärä (neliö)
# n = ympyrän sisälle jäävien pisteiden kokonaismäärä
# n/N≈π/4, josta saadaan π≈4n/N
# ympyrän yhtälö: x^2+y^2=1

import random
n = 0
toistot = 0
while toistot < 1000000:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x**2 + y**2 < 1:
        n += 1
    toistot += 1

print(f"Piin (π) likiarvo on {4*n/toistot:.2f}")