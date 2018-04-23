<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>A股每天最新新闻</title>
    </head>
    <body>
<h3><center>A股每天最新新闻</center></h3>
<?php
$host="qdm225205669.my3w.com";
$user="qdm225205669";
$password="123456qA";
//$link=mysql_connect($host,$user,$password);
$link=mysql_connect($host,$user,$password);
if(!$link) echo "没有连接成功!".'<br>';
else {
echo	'<h3><center>今天是'.date('Y-m-d').'</center></h3>';
}
$dates=date_create(date("Y-m-d"));
date_sub($dates,date_interval_create_from_date_string("2 days"));
$t= date_format($dates,"Y-m-d");
// $date=date("Y-m-d");
//echo $t;
// $todays=date_create('2018-04-13');
// echo $todays;
// date_sub($date,date_interval_create_from_date_string("20 days"));
// date_format($todays,"Y-m-d");
// // echo 'last';
// echo $todays;
mysql_select_db("qdm225205669_db", $link);
$q="SELECT * FROM tb_cnstock where `Date`> \"$t\" order by `Date` desc";             
//echo $q;
mysql_query("SET NAMES UTF8");           
$rs = mysql_query($q, $link);                     
if(!$rs){die("Valid result!");}  
echo "<table align=\"center\" border=\"1\">";
echo "<tr><td>发布日期</td><td>新闻内容</td><td>链接</td></tr>";
while($row = mysql_fetch_row($rs)) 
	{
		echo "<tr><td>$row[0]</td><td>$row[1]</td><td>$row[2]</td></tr>";
}
echo "</table>";  
mysql_free_result($rs);        
?>
<h4><center>Rocky Chen All Rights. Email: weigesysu@qq.com</center></h4>
 </body>
</html>	
