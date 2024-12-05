<?php
  ini_set('display_errors','on');
  $connect = new PDO("mysql:dbname=stage;host=192.168.56.200","bob","azerty") or die ("Pb");
  echo "Connexion OK\n";
?>

