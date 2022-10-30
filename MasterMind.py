import bottle, model

SKRIVNOST = 'Bruce Wayne je Batman'
LAHKA_IGRA = 6
TEZKA_IGRA = 9
IME_JE_ZE_V_UPORABI = 'To uporabnisko ime je že v uporabi, izberi si drugega'
IZZIV_USPEL = 'Izziv je bil uspešno poslan.'
NEVELJAVNO_IME = 'Ta uporabnik ne obstaja.'
NEVELJAVNA_KODA = 'Ta koda je neveljavna.'

mastermind = model.MasterMind()
mastermind.nalozi_igre_iz_datoteke()

@bottle.get("/")
def indeks():
    return bottle.template("views/index.tpl")

@bottle.post("/seme/")
def seme():
    seme = bottle.request.forms.seme
    koda = bottle.request.forms.koda
    napacno_seme = ''
    vrnjeno_seme = ''
    if seme and model.dobro_seme(seme):
        id_igre = mastermind.nova_igra(TEZKA_IGRA, model.NE, seme)
        uporabnisko_ime = bottle.request.get_cookie('uporabnisko_ime', secret = SKRIVNOST)
        if uporabnisko_ime:
            model.dodaj_nove_podatke(uporabnisko_ime)
        mastermind.zapisi_igre_v_datoteko()
        bottle.response.set_cookie('id_igre', id_igre, path='/', secret = SKRIVNOST)
        return bottle.redirect("/igra/")
    elif seme and not model.dobro_seme(seme):
        napacno_seme = 'Neveljavno seme, poskusi še enkrat.'
    elif koda and model.dobra_koda(koda):
        vrnjeno_seme = model.sifriraj_seme(koda)
    elif not koda:
        pass
    else:
        vrnjeno_seme = 'Neveljavna koda, poskusi še enkrat'
    return bottle.template("views/seme.tpl", {"vrnjeno_seme": vrnjeno_seme, "napacno_seme": napacno_seme})

@bottle.post("/seme/<seme:re:.*>")
def igraj_seme(seme):
    seme = seme[1:-1]
    id_igre = mastermind.nova_igra(TEZKA_IGRA, model.NE, seme)
    mastermind.zapisi_igre_v_datoteko()
    bottle.response.set_cookie('id_igre', id_igre, path='/', secret = SKRIVNOST)
    uporabnisko_ime = bottle.request.get_cookie('uporabnisko_ime', secret = SKRIVNOST)
    if uporabnisko_ime:
            model.dodaj_nove_podatke(uporabnisko_ime)
    return bottle.redirect("/igra/")

@bottle.post("/brisi_izziv/<seme:re:.*>/<izzivalec:re:.*>/")
def brisi_izziv(seme, izzivalec):
    uporabnisko_ime = bottle.request.get_cookie('uporabnisko_ime', secret = SKRIVNOST)
    izzivalec = izzivalec[1:]
    seme = seme[1:-1]
    model.brisi_izziv(uporabnisko_ime, seme, izzivalec)
    return bottle.redirect("/profil/")


@bottle.post("/lahka_igra/") 
def nova_igra():
    id_igre = mastermind.nova_igra(LAHKA_IGRA, model.JA)
    mastermind.zapisi_igre_v_datoteko()
    bottle.response.set_cookie('id_igre', id_igre, path='/', secret = SKRIVNOST)
    uporabnisko_ime = bottle.request.get_cookie('uporabnisko_ime', secret = SKRIVNOST)
    if uporabnisko_ime:
            model.dodaj_nove_podatke(uporabnisko_ime)    
    return bottle.redirect("/igra/")

@bottle.post("/srednja_igra/") 
def nova_igra():
    id_igre = mastermind.nova_igra(LAHKA_IGRA)
    mastermind.zapisi_igre_v_datoteko()
    bottle.response.set_cookie('id_igre', id_igre, path='/', secret = SKRIVNOST)
    uporabnisko_ime = bottle.request.get_cookie('uporabnisko_ime', secret = SKRIVNOST)
    if uporabnisko_ime:
            model.dodaj_nove_podatke(uporabnisko_ime)
    return bottle.redirect("/igra/")

@bottle.post("/tezja_igra/") 
def nova_igra():
    id_igre = mastermind.nova_igra(TEZKA_IGRA)
    mastermind.zapisi_igre_v_datoteko()
    bottle.response.set_cookie('id_igre', id_igre, path='/', secret = SKRIVNOST)
    uporabnisko_ime = bottle.request.get_cookie('uporabnisko_ime', secret = SKRIVNOST)
    if uporabnisko_ime:
        model.dodaj_nove_podatke(uporabnisko_ime)
    return bottle.redirect("/igra/")

@bottle.post("/pomoc/") 
def pomoc():
  return bottle.template("pomoc")

@bottle.post("/") 
def index():
  return bottle.template("index")

@bottle.get("/igra/")
def pokazi_igro():
    id_igre = bottle.request.get_cookie('id_igre', secret = SKRIVNOST)
    igra, stanje, variacija = mastermind.igre[id_igre]
    resitev = igra.resitev
    poskusi = igra.poskusi
    namigi = igra.namigi
    dovoljeno = igra.dovoljeno
    stevilke = igra.stevilke
    produkt = igra.produkt
    vsota = igra.vsota
    uporabnisko_ime = bottle.request.get_cookie('uporabnisko_ime', secret = SKRIVNOST)
    if stanje == model.ZMAGA and uporabnisko_ime:
        model.dodaj_nove_podatke(uporabnisko_ime, 1, 1, 0, len(poskusi))
    elif stanje == model.PORAZ and uporabnisko_ime:
        model.dodaj_nove_podatke(uporabnisko_ime, 1, 0, 1)
    return bottle.template("views/igra.tpl", {'resitev': resitev,'stanje': stanje,'model': model, 'poskusi': poskusi, 'namigi': namigi, 'dovoljeno': dovoljeno, 'stevilke': stevilke, 'produkt': produkt, 'vsota': vsota, 'variacija': variacija}) 

@bottle.post("/igra/")
def ugibaj():
    id_igre = bottle.request.get_cookie('id_igre', secret = SKRIVNOST)
    resitev = bottle.request.get_cookie('resitev', secret = SKRIVNOST)
    koda = bottle.request.forms.koda
    if len(str(koda)) == len(str(resitev)) and koda.isnumeric():
        mastermind.ugibaj(id_igre, koda)
    mastermind.zapisi_igre_v_datoteko()
    return bottle.redirect("/igra/")
 #####

@bottle.get("/profil/<napaka:re:.*>")
def profil(napaka):
    uporabnisko_ime = bottle.request.get_cookie('uporabnisko_ime', secret = SKRIVNOST)
    if uporabnisko_ime:
        (_, vse_igre, zmage, porazi, povprecje, izzivi) = model.preberi_uporabnika(uporabnisko_ime)
        return bottle.template("views/profil.tpl", {'uporabnisko_ime': uporabnisko_ime, 'vse_igre': vse_igre, 'zmage': zmage, 'porazi': porazi, 'povprecje': povprecje, 'izzivi': izzivi, 'napaka': napaka})
    else:
        return bottle.redirect("/vpis/")

@bottle.get("/vpis/")
def vpis():
    napaka = ''
    return bottle.template("views/vpis.tpl", {'napaka': napaka})

@bottle.post("/login")
def do_login():
    uporabnisko_ime = bottle.request.forms.uporabnisko_ime
    geslo = bottle.request.forms.geslo
    stanje_uporabnika = model.je_uporabnik(uporabnisko_ime, geslo)
    if stanje_uporabnika == model.USPESNA_PRIJAVA:
        bottle.response.set_cookie('uporabnisko_ime', uporabnisko_ime, path='/', secret = SKRIVNOST)
        return bottle.redirect("/profil/")
    elif stanje_uporabnika == model.NEVELJAVNO_GESLO:
        return bottle.template("views/vpis.tpl", {'napaka': stanje_uporabnika})
    else:
        return bottle.template("views/vpis.tpl", {'napaka': stanje_uporabnika})

@bottle.get("/registracija/")
def registracija():
    napaka = ''
    return bottle.template("views/registracija.tpl", {'napaka': napaka})

@bottle.post("/registracija/")
def registracija():
    uporabnisko_ime = bottle.request.forms.uporabnisko_ime
    geslo = bottle.request.forms.geslo
    if not uporabnisko_ime:
        napaka = ''
        return bottle.template("views/registracija.tpl", {'napaka': napaka})
    elif model.je_uporabnik(uporabnisko_ime, geslo) != model.NISI_REGISTRIRAN:
        return bottle.template("views/registracija.tpl", {'napaka' : IME_JE_ZE_V_UPORABI})
    else:
        uporabnisko_ime = model.dodaj_uporabnika(uporabnisko_ime, geslo)
        bottle.response.set_cookie('uporabnisko_ime', uporabnisko_ime, path='/', secret = SKRIVNOST)
        return bottle.redirect("/profil/")

@bottle.post("/poslji_izziv/")
def poslji_izziv():
    uporabnisko_ime = bottle.request.forms.uporabnisko_ime
    koda = bottle.request.forms.koda
    seme = model.sifriraj_seme(koda)
    ime_poslijatelja = bottle.request.get_cookie('uporabnisko_ime', secret = SKRIVNOST)
    izziv = (ime_poslijatelja, seme)
    if model.je_uporabnik(uporabnisko_ime, '') == model.NEVELJAVNO_GESLO and model.dobra_koda(koda):
        model.dodaj_nove_podatke(uporabnisko_ime, 0, 0, 0, 0, izziv)
        napaka = IZZIV_USPEL
        return bottle.redirect(f"/profil/{napaka}")
    elif model.je_uporabnik(uporabnisko_ime, '') != model.NEVELJAVNO_GESLO:
        napaka = NEVELJAVNO_IME
        return bottle.redirect(f"/profil/{napaka}")
    elif not model.dobra_koda(koda):
        napaka = NEVELJAVNA_KODA
        return bottle.redirect(f"/profil/{napaka}")  

@bottle.get("/img/<picture>")
def slika(picture):
    return bottle.static_file(picture, root="img")      
    

bottle.run(reloader = True, debug = True)