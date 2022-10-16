%rebase('base.tpl', title='MasterMind')
 <style>
* {
  box-sizing: border-box;
}


.column {
  float: left;
  padding: 10px;
  height: 600px; /* Should be removed. Only for demonstration */
}
<!
.left {
  width: 35%;
}

.right {
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
<h2>Igralna plošča</h2>
<div class="row">
  <div class="column" style="background-color:gray;">
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
  <div class="column" style="background-color:gray;">
    % for namig in namigi:
        {{namig}} <br>
    % end
  </div>
  <div class="column right" style="background-color:#654321;">
    <img src="/img/normalno.jpg" alt="2Ring">
    <p>Some text..</p>
  </div>
</div>