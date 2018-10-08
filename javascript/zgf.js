var dynamicurl = "/L3NoaXhpbi9kaXNEZXRhaWw/aWQ9MTI2MzQzMTU1JnBDb2RlPSUzQ1Jlc3BvbnNlJTIwWzIwMF0lM0UmY2FwdGNoYUlkPTEzYzVjZDEwOTE1ZjQyNjA4MGM1M2ZhMGE3ZDM1OWQ4";
var wzwschallenge = "RANDOMSTR3612";
var wzwschallengex = "STRRANDOM3612";
var template = 4;
var encoderchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";

function KTKY2RBD9NHPBCIHV9ZMEQQDARSLVFDU(str) {
    var out, i, len;
    var c1, c2, c3;
    len = str.length;
    i = 0;
    out = "";
    while (i < len) {
        c1 = str.charCodeAt(i++) & 0xff;
        if (i == len) {
            out += encoderchars.charAt(c1 >> 2);
            out += encoderchars.charAt((c1 & 0x3) << 4);
            out += "==";
            break;
        }
        c2 = str.charCodeAt(i++);
        if (i == len) {
            out += encoderchars.charAt(c1 >> 2);
            out += encoderchars.charAt(((c1 & 0x3) << 4) | ((c2 & 0xf0) >> 4));
            out += encoderchars.charAt((c2 & 0xf) << 2);
            out += "=";
            break;
        }
        c3 = str.charCodeAt(i++);
        out += encoderchars.charAt(c1 >> 2);
        out += encoderchars.charAt(((c1 & 0x3) << 4) | ((c2 & 0xf0) >> 4));
        out += encoderchars.charAt(((c2 & 0xf) << 2) | ((c3 & 0xc0) >> 6));
        out += encoderchars.charAt(c3 & 0x3f);
    }
    return out;
}