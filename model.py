import random
import json

ST_POSKUSOV = 11
STEVILKE = 6
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
NORMALNO = 'Normalno'
POUCEVALNO = "poucevalno"
ZALOSTNO = "zalostno"
ZBEGANO = "zbegano"

class Igra:

    def __init__(self, resitev, stevilke = STEVILKE, poskusi = None, namigi = None, dovoljeni_poskusi = ST_POSKUSOV):
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
    for n in range(len(resitev)):
        if resitev[n] == poskus[n]:
            namig += PRAV
        elif poskus[n] in resitev and resitev[n] != poskus[n]:
            namig += SKORAJ
        else:
            namig += NAROBE
    sortiran_namig = sorted(namig)
    sortiran_namig = ' '.join(sortiran_namig)
    return sortiran_namig

def random_koda(dol_kode, st_stevilk):
    koda = ""
    for _ in range(1, dol_kode + 1):
        koda += str(random.randrange(st_stevilk))
    return koda

def sifriraj_seme(koda):
    return koda * KODIRNO_PRAŠTEVILO

def desifriraj_seme(seme): 
    return seme // KODIRNO_PRAŠTEVILO

def nova_igra(st_stevilk, dol_kode = 4, seme = None):
    if seme == None:
        koda = random_koda(dol_kode, st_stevilk)
    else:
        koda = desifriraj_seme(seme)
    return Igra(koda, st_stevilk, [], [])
    
class MasterMind:
    datoteka_s_stanjem = DATOTEKA_S_STANJEM

    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        id = random.randint(1000000, 9999999)
        while id in self.igre:
            id = random.randint()
        return id

    def nova_igra(self, st_cifer):
        i = self.prost_id_igre()
        igra = nova_igra(st_cifer)
        self.igre[i] = (igra, ZACETEK)
        return i

    def ugibaj(self, i, poskus):
        igra, stanje = self.igre[i]
        stanje = igra.nov_poskus(poskus)
        self.igre[i] = (igra, stanje)

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem) as d:
            slovar = json.load(d)
        for id_igre, ((resitev, poskusi), namigi, st_stevilk, dovoljeno, stanje) in slovar.items():
            self.igre[id_igre] = (Igra(resitev, st_stevilk, dovoljeno, poskusi, namigi), stanje)

    

    def zapisi_igre_v_datoteko(self):
        slovar = {}
        for id_igre, (igra, stanje)  in self.igre.items():
            slovar[id_igre] = ((igra.resitev, igra.poskusi), igra.namigi, igra.stevilke, igra.dovoljeno, stanje)
        with open(self.datoteka_s_stanjem, 'w') as d:
            json.dump(slovar, d)


