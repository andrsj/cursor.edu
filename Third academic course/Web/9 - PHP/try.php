<!DOCTYPE html>
<html>
<body>

<?php
echo "Hello World" . "<br>";
?>
 <br>
<?php
echo "Today is " . date("Y/m/d") . "<br>";
echo "Day - " . date("l"). "<br>". "<br>";
?>
<br>

<?php 
$n=171239;
$b=0;
$C = array();
echo $n . "<br>";
while($n>=1)
{
    $b=$n%10;
    $n=$n/10;
    array_push($C, $b);

} 
echo implode (" ", $C);
/*
foreach($s in $C){
	array_search(reset($C), $C)
*/

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
	
$string = "I try to make something good"; 
echo "Original String :\n".$string."<br>";
$split=explode(" ", $string); 
sort($split); 
echo "After sort:\n";
echo implode(" ", $split). "<br>". "<br>"; 

?>

</body>
</html>