<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>perry the platypus 4</title>
</head>

<body>
    <img src="perry_the_platypus.png" alt="perry the platypus">
</body>

</html>
<?php
$agent = $_SERVER['HTTP_USER_AGENT'];
echo "<br>";
echo $agent;
echo "<br>";

if (preg_match('/Mozilla\/[42].+MSIE [432].\d{1,2}.+/i',$agent)) {
    $ie = 'yes';
} else {
    $ie = 'no';
}

if($ie == 'yes') {
    echo "GCTF{gr347_j0b_AgEnT_p!}";
} else {
    echo "This is not my favourite browser :(, i prefer something more... antiquated and preferably by Microsoft ";
}

?>
