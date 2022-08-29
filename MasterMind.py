import bottle, model

SKRIVNOST = 'Bruce Wayne je Batman'

mastermind = model.MasterMind
@bottle.get("/")
def indeks():
    return bottle.template("views/index.tpl")

@bottle.post("/nova_igra/") 
def nova_igra():
    id_igre = mastermind.nova_igra()
    mastermind.zapisi_igre_v_datoteko()
    bottle.response.set_cookie('id_igre', id_igre, path='/', secret = SKRIVNOST) #path je da se piškotek zapomni za vse strani
    return bottle.redirect("/igra/")

@bottle.get("/igra/")
def pokazi_igro():
    id_igre = bottle.request.get_cookie('id_igre', secret = SKRIVNOST)
    igra, stanje = mastermind.igre[id_igre]
    resitev = igra.resitev
    poskusi = igra.poskusi
    namigi = igra.namigi
    dovoljeno = igra.dovoljeno
    barve = igra.barve
    return bottle.template("views/igra.tpl", {'resitev': resitev,'stanje': stanje, 'poskusi': poskusi, 'namigi': namigi, 'dovoljeno': dovoljeno, 'barve': barve})

@bottle.post("/igra/")
def ugibaj():
    id_igre = bottle.request.get_cookie('id_igre', secret = SKRIVNOST)
    resitev = bottle.request.get_cookie('resitev', secret = SKRIVNOST)
    poskus = bottle.request.forms.poskus #praša če je kej pršlo in če je naj da crko
    if len(poskus) == len(resitev)  and poskus.isnumeric():
        mastermind.ugibaj(id_igre, poskus)
    mastermind.zapisi_igre_v_datoteko()
    return bottle.redirect("/igra/")

@bottle.get("/img/<picture>")
def slika(picture):
    return bottle.static_file(picture, root="img")

bottle.run(reloader=True, debug=True)