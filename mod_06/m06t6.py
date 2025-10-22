from math import pi

def yksikkohinta(h, eur):
    return eur / (pi * (h/2/100) ** 2)

print("1. pizza:")
pizza1 = yksikkohinta(float(input("Halkaisija (cm): ")), float(input("Hinta (eur): ")))
print("2. pizza:")
pizza2 = yksikkohinta(float(input("Halkaisija (cm): ")), float(input("Hinta (eur): ")))
if pizza1 < pizza2:
    print("1. pizzalla alhaisempi yksikköhinta.")
elif pizza1 > pizza2:
    print("2. pizzalla alhaisempi yksikköhinta.")
else:
    print("Samanhintaiset.")



"""
#2. vaihtoehto for-loopilla:
alhaisin = None
numero = 0
for i in range(2):
    pizza = yksikkohinta(float(input("Halkaisija (cm): ")), float(input("Hinta (eur): ")))
    if alhaisin is None or pizza < alhaisin:
        alhaisin = pizza
        numero = str(i+1)
    elif pizza == alhaisin:
        numero += ", " + str(i+1)
if len(numero) == 1:
    print(f"{numero}. pizzalla on alhaisin yksikköhinta.")
else:
    print(f"Pizzat {numero} ovat samanhintaisia.")
"""