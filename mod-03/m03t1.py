pituus = float(input("Anna kuhan pituus senttimetreinä: "))
if pituus < 37:
    print(f"Kuha on {37-pituus} cm alle sallitun pyyntimitan. Laske kuha takaisin järveen.")
else:
    print("Kuha hyväksytty.")