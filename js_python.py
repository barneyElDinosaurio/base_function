# -*-coding=utf-8-*-
import execjs


def demo1():
    print(execjs.get().name)
    sentence = '''
    var ztlx="有限责任公司(自然人投资或控股)";
                        var zczb="200.0000";
                                    if(zczb!=""){
                                        if(ztlx == "个体户" || ztlx == "农民专业合作经济组织"){
                                            document.write(zczb+"元");
                                        }else{
                                            document.write(zczb+"万元");
                                        }
                                    }
                                    var zcbz ="";
                                    if(zcbz==""){
                                        document.write("（人民币）");
                                    }else{
                                        document.write("（"+zcbz+"）");
                                    }
    '''

    ret = execjs.eval(sentence)
    print(ret)


def demo2():
    # 获取guid参数
    js1 = '''
    		function getGuid() {
    			var guid = createGuid() + createGuid() + "-" + createGuid() + "-" + createGuid() + createGuid() + "-" + createGuid() + createGuid() + createGuid(); //CreateGuid();
    			console.log(guid)
    			return guid;
    		}
    		var createGuid = function () {
    			return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
    		}
    		var test = function () {
    		    var t = (1 + Math.random()) * 0x10000
    		    console.log(t)
    			return t;
    		}
    	'''
    ctx1 = execjs.compile(js1)
    guid = (ctx1.call("getGuid"))
    print(guid)


from Naked.toolshed.shell import execute_js, muterun_js
import sys


def demo3():
    js = '''
    var x = 10;
    x = 10 - 5;
    console.log(x);
    function greet() {
          console.log("Hello World!");
    }
    greet()'''

    response = muterun_js(js)
    if response.exitcode == 0:
        print(response.stdout)
    else:
        sys.stderr.write(response.stderr)


demo3()
