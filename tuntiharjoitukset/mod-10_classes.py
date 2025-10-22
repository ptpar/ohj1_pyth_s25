class Hissi:
    def __init__(self, alin, ylin, nyk_kerros=0):
        self.alin = alin
        self.ylin = ylin
        self.nyk_kerros = nyk_kerros

    def kerros_ylos(self, muutos):
        for i in range(muutos):
            self.nyk_kerros += 1
            if self.nyk_kerros == self.ylin:
                break

    def kerros_alas(self, muutos):
        for i in range(muutos):
            self.nyk_kerros -= 1
            if self.nyk_kerros == self.alin:
                break

    def siirry_kerrokseen(self, kohdekerros):
        if self.nyk_kerros <= kohdekerros:
            self.kerros_ylos(kohdekerros - self.nyk_kerros)
        elif kohdekerros <= self.nyk_kerros:
            self.kerros_alas(self.nyk_kerros - kohdekerros)
        print("Hissi on kerroksessa", self.nyk_kerros)

class Talo:
    def __init__(self, alin, ylin, hissi_lkm):
        self.hissit = []
        self.lisaa_hissit(alin, ylin, hissi_lkm)

    def lisaa_hissit(self, alin, ylin, hissi_lkm):
        for i in range(hissi_lkm):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissia(self, hissi_nro, kohdekerros):
        self.hissit[hissi_nro].siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        for h in self.hissit:
            h.siirry_kerrokseen(0)

"""class Talo:
    def __init__(self, alin, ylin, hissi_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissi_lkm = hissi_lkm
        self.hissit = []
        self.lisaa_hissit()

    def lisaa_hissit(self):
        for i in range(self.hissi_lkm):
            self.hissit.append(Hissi(self.alin, self.ylin))"""
