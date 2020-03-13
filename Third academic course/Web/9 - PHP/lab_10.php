<?php
echo "<html><body>"; 
echo "<h1>Hello, World!</h1>"; 
echo "Today is " . date("Y-m-d") . "<br>";
echo "Today is " . date("l") . "<br>";
$n=1211324; // наше початкове число
$t=$n; // шукаємо першу чифру числа
while ($t>0) {
 $r=$t%10; $t=floor($t/10);}
$t=$n; // порівнюємо першу цифру числа з іншии
while ($t>0)
{
 $k=$t%10; $t=floor($t/10); 
 if ($k==$r) {$a++;} }
echo("Цифра $r зустрічається в числі $n - $a раз<br>" ); 

$A = array("a"=>"Max", "b"=>"Sasha", "c"=>"Ivan", "d"=>"Postavte_51");
foreach($A as $k=>$v) echo "| $v |" . "<br>";
asort($A);

foreach($A as $k=>$v) echo "| $v |";

$input = array(1,2,3,4,5,6);
$reversed = array_reverse($input);
print_r($input);
print_r($reversed);

$string = "Mykola likes Anabel"; //any string
echo "Original String :\n".$string."<br>";
$split=explode(" ", $string); // breaks sentence in to elements

 // $split[0] will be code

sort($split); // sorts the elements
echo "After sort:\n";
echo implode(" ", $split). "<br>". "<br>";


$n=1211324; // наше початкове число
$t=$n; // шукаємо першу чифру числа
$Array;
while ($t>0) {
 $r=$t%10; $t=floor($t/10);}
$t=$n; // порівнюємо першу цифру числа з іншии
while ($t>0)
{
	
  }
echo("Цифра $r зустрічається в числі $n - $a раз<br>" ); 
echo "</body></html>"; 
?>