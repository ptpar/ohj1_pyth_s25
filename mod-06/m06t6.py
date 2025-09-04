from math import pi

def yksikkohinta(h, eur):
    return eur / (pi * (h/2/100) ** 2)

print("1. pizza:")
pizza1 = yksikkohinta(float(input("Halkaisija (cm): ")), float(input("Hinta (eur): ")))
print("2. pizza:")
pizza2 = yksikkohinta(float(input("Halkaisija (cm): ")), float(input("Hinta (eur): ")))
if pizza1 < pizza2:
    print("1. pizzalla alhaisempi yksikköhinta.")
else:
    print("2. pizzalla alhaisempi yksikköhinta.")



"""
#2. vaihtoehto for-loopilla:
alhaisin = None
numero = 0
for i in range(2):
    pizza = yksikkohinta(float(input("Halkaisija (cm): ")), float(input("Hinta (eur): ")))
    if alhaisin is None or pizza < alhaisin:
        alhaisin = pizza
        numero = i+1
print(f"{numero}. pizzalla on alhaisin yksikköhinta.")
"""