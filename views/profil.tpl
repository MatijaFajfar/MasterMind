%rebase('base.tpl', title='MasterMind')

<h1> Profil </h1>
<img src="/img/Normalno.jpg" alt="2Ring">
<p> Živjo, {{uporabnisko_ime}}! <br>
Tu lahko najdeš podatke o svojih igrah, igraš izzive in pošiljaš izzive drugim uporabnikom.
<h2> Podatki </h1>
<ul>
    <li> Začete igre: {{vse_igre}} </li>
    <li> Zmage: {{zmage}} </li>
    <li>Porazi: {{porazi}} </li>
    <li> Povprečno število poskusov do zmage: {{povprecje}} </li>
</ul>

<h2> Tvoji izzivi </h2>
%if izzivi == []:
    <p> Izgleda, da še nisi prejel nobenega izziva. </p>
%else:
    for (uporabnik, seme) in izzivi:
    <ul>
        <li> {{uporabnik}} ti je poslal to seme: 
            <form action="/seme/<{{seme}}>/" method="post">
                <button type="submit">Igraj</button>
            </form>
        </li>
%end

<h2> Pošlji izziv </h2>
<p>
<form action="/poslji_izziv/" method="post">
            Uporabniško ime: <input name="uporabnisko_ime" type="text" />
            Koda: <input name="koda" type="text" />
            <input value="Pošlji izziv" type="submit" />
        </form> 
{{napaka}}
</p>
