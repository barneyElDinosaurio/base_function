<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>A股黑名单</title>
    </head>
    <body>
<?php
$link=mysql_connect("localhost","root","");   
if(!$link) echo "没有连接成功!";   
else echo "连接成功!"; 
?> 

<?php  
mysql_select_db("db_stock", $link);          //选择数据库  
$q = "SELECT * FROM tb_blacklist";                   //SQL查询语句  
mysql_query("SET NAMES UTF8");           
$rs = mysql_query($q, $link);                     //获取数据集  
if(!$rs){die("Valid result!");}  
echo "<table>";  
echo "<tr><td>日期</td><td>代码</td><td>名称</td><td>拉黑原因</td></tr>";  
while($row = mysql_fetch_row($rs)) echo "<tr><td>$row[0]</td><td>$row[1]</td><td>$row[2]</td><td>$row[3]</td></tr>";   //显示数据  
echo "</table>";  
mysql_free_result($rs);                    //关闭数据集  
?> 
  
 </body>
</html>	
