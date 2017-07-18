#-*-coding=utf-8-*-
import seaborn as sns

def testcase1():
    tips=sns.load_dataset('tips')
    sns.jointplot('total_bill','tips',tips,kind='reg')

testcase1()