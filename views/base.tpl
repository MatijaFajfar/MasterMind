<!DOCTYPE html>
<html>
<style>
* {
 font-size: 100%;
 font-family: Arial;
}

body {
  padding-left: 20px;
  padding-right: 20px;
}

h1 {
  font-size: 30px;
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

button {
    background-color: #04AA6D; 
  border: 1px solid green;
  color: white;
  padding: 10px 24px;
  cursor: pointer;
  float: left;
}

input {
    background-color: #04AA6D; 
  border: 1px solid green;

}

.right {
  width: 25%;
}
.btn-group button {
  background-color: #04AA6D; 
  border: 1px solid green;
  color: white;
  padding: 10px 24px;
  cursor: pointer;
  float: left;
}

.btn-group button:not(:last-child) {
  border-right: none;
}

.btn-group:after {
  content: "";
  clear: both;
  display: table;
}

.btn-group button:hover {
  background-color: #3e8e41;
}
</style>

<head>
<meta charset="UTF-8">
    <title> {{title}} </title>
</head>
<body style="background-color: gray">
  <h1>MasterMind</h1>

  <div class="btn-group">
    <form action="/" method="post">
      <button type="submit">Meni</button>
    </form>

    <form action="/lahka_igra/" method="post">
      <button type="submit">Lahka igra</button>
      </form>

    <form action="/srednja_igra/" method="post">
      <button type="submit">Srednja igra</button>
      </form>

    <form action="/tezja_igra/" method="post">
      <button type="submit">Težja igra</button>
      </form>

    <form action="/seme/" method="post">
      <button type="submit">Seme</button>
      </form>

    <form action="/pomoc/" method="post">
      <button type="submit">Pomoč</button>
      </form>

    <form action="/profil/" method="get">
      <button type="submit">Profil</button>
      </form>
  </div>

</div> 
{{!base}}

</body>

</html>