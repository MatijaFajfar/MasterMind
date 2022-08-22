ST_POSKUSOV = 12
ST_BARV = 6
DOL_KODE = 4
ZMAGA = 'O'
PORAZ = 'X'
NADALJUJ = 'I'
PRAV = 'R'
SKORAJ = 'B'
NAROBE = 'C'

class Igra:

    def __init__(self, resitev, poskusi = [], namigi = [], barve = ST_BARV, dovoljeni_poskusi = ST_POSKUSOV):
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