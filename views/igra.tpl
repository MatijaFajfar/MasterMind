%rebase('base.tpl', title='MasterMind')
 <style>
* {
  box-sizing: border-box;
}


img {
  width: 100%;
  height: auto;
}

.column {
  float: left;
  padding: 10px;
  height: auto;
  font-size:40px
}
<!
.left {
  width: 40%;
}

.right {
  width: 25%;
}
.middle {
  padding: 55px;
  width: 35%;
}
>
.row:after {
  content: "";
  display: table;
  clear: both;
}
</style>

<body>
<h1>Igralna plošča</h1>
<div class="row">
  <div class="column left" style="background-color:gray;">
    <p>

    % for poskus in poskusi:
        {{poskus}} <br>
    % end

    % if stanje != model.ZMAGA and stanje != model.PORAZ:
    <form action ="" method="post">
    <input name="koda" autofocus> <input type="submit" value="Ugibaj"> 
  	<form/>      
    </p>

    % else:
    <form action="/lahka_igra/" method="post">
    <button type="submit">Nova igra?</button>
    </form>
    % end

    
  </div>
  <div class="column middle" style="background-color:gray;">
    % for namig in namigi:
        {{namig}} <br>
    % end
  </div>
  <div class="column right" style="background-color:#654321;">
    %if stanje == model.ZMAGA and len(poskusi) <= 6:
    <img src="/img/normalno.jpg" alt="2Ring">
      <p> Bravo! Presenečen sem, kako dobro ti je šlo. Sam zmorem vsako kodo rešiti tako hitro, zato predlagam, da poskusiš še kakšno igro in se še bolj izuriš. </p>
    %elif stanje == model.ZMAGA:
    <img src="/img/normalno.jpg" alt="2Ring">
      <p> Super! Uspelo ti je v {{len(poskusi)}} poskusih! Poskusi to izboljšati z igranjem še ene igre! </p>
    %elif stanje == model.PORAZ:
    <img src="/img/zalostno.jpg" alt="2Ring">
      <p> Srce se mi para, ko vidim tak poraz. Ne krivim tebe, ampak svoje učiteljske sposobnosti. Ponovno preberi navodila, nato pa predlagam ponoven poskus. </p>
    %elif len(poskusi) == 3 * int(dovoljeno) // 4:
    <img src="/img/normalno.jpg" alt="2Ring">
      <p> Ne ostaja ti veliko poskusov, zato izvoli namig. Zmnožek cifer v kodi je enak {{produkt}}. </p>
    %elif variacija == model.JA:
    <img src="/img/normalno.jpg" alt="2Ring">
      <p> Moj nasvet za to rundo je tak: vsota števk v rešitvi je enaka {{vsota}}.
    %else:
    <img src="/img/normalno.jpg" alt="2Ring">
      <p> Ne pozabi, imaš {{dovoljeno + 1}} poskusov, v rešitvi pa so številke od 0 do {{stevilke}}
  </div>
</div>