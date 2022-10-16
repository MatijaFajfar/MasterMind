import random
import json

ST_POSKUSOV = 11
STEVILKE = 6
DOL_KODE = 4
ZMAGA = 'ZMAGA'
PORAZ = 'PORAZ'
NADALJUJ = 'I'
PRAV = 'P'
SKORAJ = 'N'
NAROBE = 'X'
KODIRNO_ŠTEVILO_1 = 5915587277
KODIRNO_ŠTEVILO_2 = 42
DATOTEKA_S_STANJEM = "stanje.json"
ZACETEK = 'ZACETEK'
JA = 'JA'
NE = 'NE'

class Igra:

    def __init__(self, resitev, stevilke = STEVILKE, poskusi = None, namigi = None, variacija = NE, dovoljeni_poskusi = ST_POSKUSOV):
        if poskusi is None:
            self.poskusi = []
        else:
            self.poskusi = poskusi
        if namigi is None:
            self.namigi = []
        else:
            self.namigi = namigi
        self.resitev = resitev
        self.stevilke = stevilke
        self.dovoljeno = dovoljeni_poskusi
        self.produkt = produkt(resitev)
        self.vsota = vsota(resitev)
        self.variacija = variacija

    def nov_poskus(self, poskus):
        self.poskusi.append(poskus)
        self.namigi.append(str(namig(self.resitev, poskus)))
        if self.zmaga():
            return ZMAGA
        elif self.poraz():
            return PORAZ
        else:
            return NADALJUJ

    def zmaga(self):
        return self.resitev in self.poskusi

    def poraz(self):
        return len(self.poskusi)> self.dovoljeno


def namig(resitev, poskus):
    namig = ""
    for n in range(len(str(resitev))):
        if str(resitev)[n] == poskus[n]:
            namig += PRAV
        elif poskus[n] in resitev and resitev[n] != poskus[n]:
            namig += SKORAJ
        else:
            namig += NAROBE
    sortiran_namig = sorted(namig)
    sortiran_namig = ' '.join(sortiran_namig)
    return sortiran_namig

def produkt(resitev):
    k = 1
    for n in str(resitev):
        k *= int(n)
    return k

def vsota(resitev):
    k = 0
    for n in str(resitev):
        k += int(n)
    return k

def random_koda(dol_kode, st_stevilk):
    koda = ""
    for _ in range(1, int(dol_kode) + 1):
        koda += str(random.randrange(st_stevilk))
    return koda

def sifriraj_seme(koda):
    return int(koda) * KODIRNO_ŠTEVILO_1 + KODIRNO_ŠTEVILO_2

def desifriraj_seme(seme):
    return str((int(seme) - KODIRNO_ŠTEVILO_2) // KODIRNO_ŠTEVILO_1)


def nova_igra(st_stevilk, variacija, seme = None, dol_kode = 4):
    if seme == None:
        koda = random_koda(dol_kode, st_stevilk)
    else:
        koda = desifriraj_seme(seme)
    return Igra(koda, st_stevilk, [], [], variacija)
    
class MasterMind:
    datoteka_s_stanjem = DATOTEKA_S_STANJEM

    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        id = random.randint(1000000, 9999999)
        while id in self.igre:
            id = random.randint()
        return id

    def nova_igra(self, st_cifer, variacija = NE, seme = None, dol_kode = 4):
        i = self.prost_id_igre()
        igra = nova_igra(st_cifer, variacija, seme, dol_kode)
        self.igre[i] = (igra, ZACETEK, variacija)
        return i

    def ugibaj(self, i, poskus):
        igra, stanje, variacija = self.igre[i]
        stanje = igra.nov_poskus(poskus)
        self.igre[i] = (igra, stanje, variacija)

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem) as d:
            slovar = json.load(d)
        for id_igre, ((resitev, poskusi), namigi, st_stevilk, dovoljeno, variacija, stanje) in slovar.items():
            self.igre[id_igre] = (Igra(resitev, st_stevilk, dovoljeno, poskusi, namigi), stanje, variacija)

    def zapisi_igre_v_datoteko(self):
        slovar = {}
        for id_igre, (igra, stanje, variacija) in self.igre.items():
            slovar[id_igre] = ((igra.resitev, igra.poskusi), igra.namigi, igra.stevilke, igra.dovoljeno, variacija, stanje)
        with open(self.datoteka_s_stanjem, 'w') as d:
            json.dump(slovar, d)


