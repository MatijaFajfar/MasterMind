%rebase('base.tpl', title='MasterMind')

<h1> Vpis</h1>
<img src="/img/zalostno.jpg" alt="2Ring">
<p> Nisi še vpisan. Vpiši se spodaj.
<form action="/login" method="post">
            Uporabniško ime: <input name="uporabnisko_ime" type="text" />
            Geslo: <input name="geslo" type="password" />
            <input value="Vpis" type="submit" />
        </form> 
{{napaka}}
</p>

<p>
Če še nisi, pa se lahko registriraš.
<form action="/registracija/" method="get">
      <button type="submit">Registriraj me!</button>
</form>

</p>