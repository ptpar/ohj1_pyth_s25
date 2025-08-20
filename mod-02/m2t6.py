from random import randint
print("Kolminumeroinen koodi:")
print("".join((str(randint(0,9)) for i in range(3))))
print("Nelinumeroinen koodi:")
print("".join((str(randint(1,6)) for j in range(4))))