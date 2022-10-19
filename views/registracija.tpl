%rebase('base.tpl', title='MasterMind')

<h1> Vpis</h1>
<img src="/img/zbegano.jpg" alt="2Ring">
<p> Izgleda, da te še nimam v svoji bazi podatkov. Spodaj se lahko registriraš.

<form action="/registracija/" method="post">
        Uporabniško ime: <input name="uporabnisko_ime" type="text" />
        Geslo: <input name="geslo" type="password" />
        <input value="Registracija" type="submit" />
    </form>
{{napaka}}

</p>