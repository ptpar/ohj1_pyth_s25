class Hissi:
    def __init__(self, alin, ylin, nyk_kerros=0):
        self.alin = alin
        self.ylin = ylin
        self.nyk_kerros = nyk_kerros

    def kerros_ylos(self):
        self.nyk_kerros += 1

    def kerros_alas(self):
        self.nyk_kerros -= 1

    def siirry_kerrokseen(self, kohdekerros):
        if self.alin > kohdekerros or kohdekerros > self.ylin:
            print("Kerrosta", kohdekerros, "ei ole.")
            return
        while self.nyk_kerros != kohdekerros:
            if self.nyk_kerros <= kohdekerros:
                self.kerros_ylos()
            elif kohdekerros <= self.nyk_kerros:
                self.kerros_alas()
        print("Hissi on kerroksessa", self.nyk_kerros)