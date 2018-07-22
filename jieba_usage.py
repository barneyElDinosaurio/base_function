#-*-coding=utf-8-*-
import jieba.posseg as pseg
import jieba.analyse

content = '''
深圳大学城图书馆2018年度年鉴采购项目（项目编号：UTL20180004）于2018年6月28日完成开标。根据评标委员会评审结果，确定深圳书城中心城实业有限公司为中标供应商，并于2018年7月2日-6日在深圳大学城图书馆官方网站进行中标公示。期间，我单位收到书面质疑说明，质疑深圳书城中心城实业有限公司与投标商深圳出版发行集团公司有直接控股关系，不符合投标资格。经招标小组和法律顾问核查及评标委员会复议，结果如下：

      根据《中华人民共和国招投标实施条例》第三十四条规定，存在控股、管理关系的不同单位，不得参加同一标段投标或者未划分标段的同一招标项目投标。违反上述规定的，相关投标无效。经核查，深圳出版发行集团公司持有深圳书城中心城实业有限公司100%股权，因此，本项质疑成立。

     综上所述，我单位决定取消深圳书城中心城实业有限公司中标供应商资格。

    特此公告。
'''

words=pseg.cut(content)
for word, flag in words:
	print u'{} {}'.format(word,flag)


result=jieba.analyse.extract_tags(content,topK=20,withWeight=True,allowPOS=())
for item in result:
	print item[0],item[1]

print('text rank')
result=jieba.analyse.textrank(content,topK=20,withWeight=True,allowPOS=('ns','n','vn','v'))
for item in result:
	print item[0],item[1]