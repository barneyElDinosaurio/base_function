# coding: utf-8
import difflib

a='abcd'
b='dcba1'
seq1=difflib.SequenceMatcher(None,a=a.lower(),b=b.lower())
seq2=difflib.SequenceMatcher(None,a,b)
d1=seq1.ratio()*100
d2=seq2.ratio()*100
print d1
print d2