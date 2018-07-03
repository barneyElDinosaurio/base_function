var json={}
var getParam = (function () {
        function ObjectSort(obj) {
            var newObject = {};
            Object.keys(obj).sort().map(function (key) {
                newObject[key] = obj[key]
            });
            return newObject
        }
        return function (method, obj) {
            var appId = '1a45f75b824b2dc628d5955356b5ef18';
            var clienttype = 'WEB';
            var timestamp = new Date().getTime();
			if(typeof (JSON)=='undefined'){
                $.getScript('json2.js')
                }
            var param = {
                appId: appId,
                method: method,
                timestamp: timestamp,
                clienttype: clienttype,
                object: obj,
                secret: hex_md5(appId + method + timestamp + clienttype + JSON.stringify(ObjectSort(obj)))
            };
            param = BASE64.encrypt(JSON.stringify(param));
            return AES.encrypt(param, aes_client_key, aes_client_iv)
        }
    })();
	
	
	function decodeData(data) {
        data = AES.decrypt(data, aes_server_key, aes_server_iv);
        data = DES.decrypt(data, des_key, des_iv);
        data = BASE64.decrypt(data);
        return data
    }
	
	
	function getEncryptedData(method, city, type, startTime, endTime) {
    var param = {};
    param.city = city;
    param.type = type;
    param.startTime = startTime;
    param.endTime = endTime;
    return getParam(method, param);
}