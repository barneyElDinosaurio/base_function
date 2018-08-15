# -*-coding=utf-8-*-
import execjs

print(execjs.get().name)
sentence ='''
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
