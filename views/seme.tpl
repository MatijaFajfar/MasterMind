%rebase('base.tpl', title='MasterMind')
    <img src="/img/normalno.jpg" alt="2Ring">
<h2> Ustvari seme </h2>
<p> Tu lahko vpišeš svojo štirimestno kodo in dobiš seme, s katerim lahko prijatelja izzoveš na težko igro. 
<form action ="" method="post">
    <input name="koda" autofocus> <input type="submit" value="Vpiši kodo"> 
  	<form/>
    Tvoje seme je: {{vrnjeno_seme}}
</p>
<h2> Uporabi seme </h2>
<p> Tu lahko vpišeš seme in zaigraš igro, katere rešitev je zašifrirana z semenom. <br>
<form action ="" method="post">
    <input name="seme" autofocus> <input type="submit" value="Začni igro"> 
  	<form/>
</p>

