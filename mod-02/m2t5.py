leiviskat = float(input("Anna leiviskät.\n"))
print()
naulat = float(input("Anna naulat.\n"))
print()
luodit = float(input("Anna luodit.\n"))
print()

#Jos haluaa tarkan vastausarvon, voisi käyttää Decimal-moduulia float-lukujen kanssa?
yht = 13.3*(luodit + naulat*32 + leiviskat*20*32)

print("Massa nykymittojen mukaan:")
if yht // 1000 > 0:
    print(f"{yht // 1000} kilogrammaa ja ", end="")
print(f"{yht % 1000:.2f} grammaa.")