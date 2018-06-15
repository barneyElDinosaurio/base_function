<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>实现最简单的php网页+mysql查询功能 Rocky</title>
    </head>
    <body>

<?php
echo date("Y/m/d h:i:s") . "<br>";
header("Content-type: text/html;charset=utf-8");
mysql_query('set names utf8');
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "db_stock";
// 创建连接
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
}
$conn->query('set names utf8') or die('query字符集错误');
$sql = "SELECT DATE, CODE, NAME FROM tb_blacklist";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // 输出数据
    while($row = $result->fetch_assoc()) {
        //echo "Date: " . $row["DATE"]. " - Code: " . $row["CODE"]. " NAME: " . $row["NAME"]. "<br>";
        echo $row["NAME"]
    }
} else {
    echo "0 结果";
}
$conn->close();
?>
    </body>
</html>