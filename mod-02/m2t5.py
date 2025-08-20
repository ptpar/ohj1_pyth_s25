from decimal import Decimal

leiviskat = float(input("Anna leiviskät.\n"))
print()
naulat = float(input("Anna naulat.\n"))
print()
luodit = float(input("Anna luodit.\n"))
print()

yht = Decimal("13.3")*(Decimal(str(luodit))+Decimal(str(naulat))*32+Decimal(str(leiviskat))*20*32)

print("Massa nykymittojen mukaan:")
if yht // 1000 > 0:
    print(f"{yht // 1000} kilogrammaa ja ", end="")
print(f"{yht % 1000} grammaa.")
