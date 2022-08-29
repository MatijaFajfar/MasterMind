import random
import json

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
DATOTEKA_S_STANJEM = "stanje.json"
ZACETEK = 'zacetek'

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
    namig = ''
    for n in range(len(resitev)):
        if resitev[n] == poskus[n]:
            namig += PRAV
            seznam += poskus[n]
        elif poskus[n] in resitev:
            namig += SKORAJ
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
    
class MasterMind:
    datoteka_s_stanjem = DATOTEKA_S_STANJEM

    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        id = random.randint()
        while id in self.igre:
            id = random.randint()
        return id

    def nova_igra(self):
        i = self.prost_id_igre()
        igra = nova_igra()
        self.igre[i] = (igra, ZACETEK)
        return i

    def ugibaj(self, i, poskus):
        igra, stanje = self.igre[i]
        stanje = igra.nov_poskus(poskus)
        self.igre[i] = (igra, stanje)

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem) as d:
            slovar = json.load(d)
        for id_igre, ((resitev, poskusi), namigi, barve, dovoljeno, stanje) in slovar.items():
            self.igre[id_igre] = (Igra(resitev, barve, dovoljeno, poskusi, namigi), stanje)


    def zapisi_igre_v_datoteko(self):
        slovar = {}
        for id_igre, (igra, stanje)  in self.igre.items():
            slovar[id_igre] = ((igra.resitev, igra.poskusi), igra.namigi, igra.barve, igra.dovoljeno, stanje)
        with open(self.datoteka_s_stanjem, 'w') as d:
            json.dump(slovar, d)