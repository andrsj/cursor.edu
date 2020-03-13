<?php
echo "<html><body>"; 
echo "<h1>Hello, World!</h1>";
echo "Today is " . date("Y-m-d") . "<br>";
echo "Today is " . date("l") . "<br>";
?>

<br>
<br>

<?php 
$n=67111239;
$b=0;
$C = array();
echo $n . "<br>";
$iter = 0;
while($n>=1)
{
    $b=$n%10;
    $n=$n/10;
    array_push($C, $b);
    $iter++;
} 
echo implode (" ", $C);
echo "<br>" . $iter . " - count";
$count = 0;
foreach($C as $i){
    if(end($C) == $i){
        $count++;
    }
}
echo "<br>" . end($C) . " repeat " . $count . " times <br>";
?> 

<br>
<br>

<?php
$H=array(70,-1,20,-9,14);
echo "Original array: " ;
echo implode(" ", $H). "<br>";
echo ("After: ");
    foreach($H as $val){
        if((gettype($val)=="integer")and($val>0)){
            $val=0;
        }
        echo($val);
        echo("\n");
    }	
?>

<br>
<br>

<?php 
$n=472;
$b=0;
echo $n . "<br>";
while($n>=1)
{
    $b=$b*10+$n%10;
    $n=$n/10;
}
echo $b;
?>

<br>
<br>

<?php
	
$string = "My name is Andrew";
echo "Original String :\n".$string."<br>";
$string = strtolower($string);
$split=explode(" ", $string); 
sort($split); 
echo "After sort:\n";
echo implode(" ", $split). "<br>". "<br>"; 

?>