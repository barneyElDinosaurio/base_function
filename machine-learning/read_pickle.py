try:
	import cPickle as pickle
except:
	import pickle

with open('linear_modle.pkl','r') as f:
	linear_modle=pickle.load(f)

