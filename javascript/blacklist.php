<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>A股黑名单</title>
    </head>
    <body>
<h3><center>A股黑名单</center></h3><br>
<?php
$link=mysql_connect("qdm225205669.my3w.com","qdm225205669","");
if(!$link) echo "没有连接成功!".'<br>';
else echo '<center>今天是'.date('Y-m-d').'</center><br>';

?> 

<?php  
mysql_select_db("qdm225205669_db", $link);          //选择数据库
$q = "SELECT * FROM tb_blacklist order by `DATE` desc";                   //SQL查询语句
mysql_query("SET NAMES UTF8");           
$rs = mysql_query($q, $link);                     //获取数据集  
if(!$rs){die("Valid result!");}  
echo "<table border=\"1\" align=\"center\">";
echo "<tr><td>加入日期</td><td>代码</td><td>名称</td><td>拉黑原因</td></tr>";
while($row = mysql_fetch_row($rs)) echo "<tr><td>$row[0]</td><td>$row[1]</td><td>$row[2]</td><td>$row[3]</td></tr>";   //显示数据  
echo "</table>";  
mysql_free_result($rs);                    //关闭数据集  
?>
 </body>
</html>	
