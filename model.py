import random

ST_POSKUSOV = 12
ST_BARV = 6
DOL_KODE = 4
ZMAGA = 'O'
PORAZ = 'X'
NADALJUJ = 'I'
PRAV = 'R'
SKORAJ = 'B'
NAROBE = 'C'
KODIRNO_PRAŠTEVILO = 5915587277

class Igra:

    def __init__(self, resitev, barve = ST_BARV, dovoljeni_poskusi = ST_POSKUSOV, poskusi = [], namigi = []):
        self.resitev = resitev
        self.poskusi = poskusi
        self.namigi = namigi
        self.barve = barve
        self.dovoljeno = dovoljeni_poskusi

    def nov_poskus(self, poskus):
        self.poskusi += poskus
        self.namigi += namig(self.resitev, poskus)
        if poskus == self.resitev:
            return ZMAGA
        elif len(self.poskusi) >= self.dovoljeno:
            return PORAZ
        else:
            return NADALJUJ

def namig(resitev, poskus):
    namig = ''
    seznam = ''
    for n in range(len(resitev)):
        if resitev[n] == poskus[n]:
            namig += PRAV
            seznam += poskus[n]
        elif resitev.count(poskus[n]) > seznam.count(poskus[n]):
            namig += SKORAJ
            seznam += poskus[n]
        else:
            namig += NAROBE
    return sorted(namig)

def random_koda(dol_kode, st_barv):
    koda = ""
    for _ in range(dol_kode):
        koda += random.randrange(st_barv)
    return koda

def sifriraj_seme(koda):
    return koda * KODIRNO_PRAŠTEVILO

def desifriraj_seme(seme): 
    return seme // KODIRNO_PRAŠTEVILO

def nova_igra(dol_kode, st_barv,st_poskusov, seme = None):
    if seme == None:
        koda = random_koda(dol_kode, st_barv)
    else:
        koda = desifriraj_seme(seme)
    return Igra(koda, st_barv, st_poskusov)
    