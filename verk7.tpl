<!DOCTYPE html>
<html lang="is"> 
  <head>
    <title>login</title>
    <meta charset="utf-8">
  </head>
  <body>
  <form method='get' action='/data' accept-charset="ISO-8859-1">

      <h2>Login</h2>
      Notendanafn:<br>
      <input type="text" name='nafn' placeholder="Notendanafn" required=""><br>
      Lykilorð:<br>
      <input type="text" name='lykilord' placeholder="****" required=""><br>

      <input type='submit' value='login'>
      <input type='reset' value='Hreinsa'>
  </form>    
  </body>
</html>