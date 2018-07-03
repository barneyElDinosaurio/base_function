function getProUrl() {
	var locationx = (location.href + '').split('/');
	var basePath = "";
	if(locationx[3] == "hljweb"){
		basePath = locationx[0] + '//' + locationx[2] + '/' + locationx[3];
	} else{
		basePath = locationx[0] + '//' + locationx[2];
	}
	/*if (location[3] == undefined || location[3] == "") {
		basePath = location[0] + '//' + location[2];
	} else if (location[3] == "pub") {
		basePath = location[0] + '//' + location[2] ;
	} else {
		basePath = location[0] + '//' + location[2] + '/' + location[3];
	}*/
	return basePath;
}


var http = require('http');
http.createServer(function (request, response) {

    // 发送 HTTP 头部
    // HTTP 状态值: 200 : OK
    // 内容类型: text/plain
    response.writeHead(200, {'Content-Type': 'text/plain'});
    var webPath = getProUrl();
    // 发送响应数据 "Hello World"
    // var s='good';

    response.end(webPath);
}).listen(9001);

// 终端打印如下信息
console.log('Server running at http://127.0.0.1:9001/');