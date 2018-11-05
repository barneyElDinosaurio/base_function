# -*-coding=utf-8-*-

# @Time : 2018/10/30 15:23
# @File : social_code_gen2.py

# -*- coding: utf-8 -*-
'''
Created on 2017年4月5日
18位统一社会信用代码从2015年10月1日正式实行

@author: rocky
'''
# 统一社会信用代码中不使用I,O,Z,S,V

SOCIAL_CREDIT_CHECK_CODE_DICT = {
                '0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
                'A':10,'B':11,'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'J':18, 'K':19, 'L':20, 'M':21, 'N':22, 'P':23, 'Q':24,
               'R':25, 'T':26, 'U':27, 'W':28, 'X':29, 'Y':30}
# GB11714-1997全国组织机构代码编制规则中代码字符集
ORGANIZATION_CHECK_CODE_DICT = {
                '0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
                'A':10,'B':11,'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17,'I':18, 'J':19, 'K':20, 'L':21, 'M':22, 'N':23, 'O':24,'P':25, 'Q':26,
               'R':27,'S':28, 'T':29, 'U':30,'V':31, 'W':32, 'X':33, 'Y':34,'Z':35}

class UnifiedSocialCreditIdentifier(object):
    '''
    统一社会信用代码
    '''

    def __init__(self):
        '''
        Constructor
        '''
    def check_social_credit_code(self,code):
        '''
        校验统一社会信用代码的校验码
        计算校验码公式:
            C9 = 31-mod(sum(Ci*Wi)，31)，其中Ci为组织机构代码的第i位字符,Wi为第i位置的加权因子,C9为校验码
        '''
        # 第i位置上的加权因子
        weighting_factor = [1,3,9,27,19,26,16,17,20,29,25,13,8,24,10,30,28]
        # 本体代码
        ontology_code = code[0:17]
        # 校验码
        check_code = code[17]
        # 计算校验码
        tmp_check_code = self.gen_check_code(weighting_factor, ontology_code, 31, SOCIAL_CREDIT_CHECK_CODE_DICT)
        if tmp_check_code==check_code:
            return True
        else:
            return False

    def check_organization_code(self,code):
        '''
        校验组织机构代码是否正确,该规则按照GB 11714编制
        统一社会信用代码的第9~17位为主体标识码(组织机构代码)，共九位字符
        计算校验码公式:
            C9 = 11-mod(sum(Ci*Wi)，11)，其中Ci为组织机构代码的第i位字符,Wi为第i位置的加权因子,C9为校验码
        @param  code: 统一社会信用代码
        '''
        # 第i位置上的加权因子
        weighting_factor = [3,7,9,10,5,8,4,2]
        # 第9~17位为主体标识码(组织机构代码)
        organization_code = code[8:17]
        # 本体代码
        ontology_code=organization_code[0:8]
        # 校验码
        check_code = organization_code[8]
        #
        print(organization_code,ontology_code,check_code)
        # 计算校验码
        tmp_check_code = self.gen_check_code(weighting_factor, ontology_code, 11, ORGANIZATION_CHECK_CODE_DICT)
        if tmp_check_code==check_code:
            return True
        else:
            return False

    def gen_check_code(self,weighting_factor,ontology_code, modulus,check_code_dict):
        '''
        @param weighting_factor: 加权因子
        @param ontology_code:本体代码
        @param modulus:  模数
        @param check_code_dict: 字符字典
        '''
        total = 0
        for i in range(len(ontology_code)):
            if ontology_code[i].isdigit():
                print(ontology_code[i] ,weighting_factor[i])
                total += int(ontology_code[i]) * weighting_factor[i]
            else:
                total += check_code_dict[ontology_code[i]]*weighting_factor[i]
        diff = modulus - total % modulus
        print(diff)
        return list(check_code_dict.keys())[list(check_code_dict.values())[diff]]



if __name__ == '__main__':
    u = UnifiedSocialCreditIdentifier()
    print(u.check_organization_code(code='92141021MA0HATBW8X'))
    print(u.check_social_credit_code(code='92141021MA0HATBW8X'))
