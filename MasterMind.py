import bottle, model

SKRIVNOST = 'Bruce Wayne je Batman'
LAHKA_IGRA = 6
TEZKA_IGRA = 9

mastermind = model.MasterMind()
mastermind.nalozi_igre_iz_datoteke()

@bottle.get("/")
def indeks():
    return bottle.template("views/index.tpl")

@bottle.post("/lahka_igra/") 
def nova_igra():
    id_igre = mastermind.nova_igra(LAHKA_IGRA, model.JA)
    mastermind.zapisi_igre_v_datoteko()
    bottle.response.set_cookie('id_igre', id_igre, path='/', secret = SKRIVNOST)
    return bottle.redirect("/igra/")

@bottle.post("/srednja_igra/") 
def nova_igra():
    id_igre = mastermind.nova_igra(LAHKA_IGRA)
    mastermind.zapisi_igre_v_datoteko()
    bottle.response.set_cookie('id_igre', id_igre, path='/', secret = SKRIVNOST)
    return bottle.redirect("/igra/")

@bottle.post("/tezja_igra/") 
def nova_igra():
    id_igre = mastermind.nova_igra(TEZKA_IGRA)
    mastermind.zapisi_igre_v_datoteko()
    bottle.response.set_cookie('id_igre', id_igre, path='/', secret = SKRIVNOST)
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

@bottle.get("/img/<picture>")
def slika(picture):
    return bottle.static_file(picture, root="img")

bottle.run(reloader = True, debug = True)