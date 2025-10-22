from .hissi import Hissi

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissi_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissi_lkm = hissi_lkm
        self.hissit = []
        for i in range(hissi_lkm):
            self.hissit.append(Hissi(self.alin_kerros, self.ylin_kerros))

    def aja_hissia(self, hissi_nro, kohdekerros):
        print(f"Hissi nro {hissi_nro}:")
        self.hissit[hissi_nro-1].siirry_kerrokseen(kohdekerros)
        print()

    def palohalytys(self):
        print("Palohälytys!")
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