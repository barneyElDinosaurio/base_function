#-*-coding=utf8-*-
import json,math

class recommander():

	def __init__(self,data,k=3,metric='pearson',n=5):
		self.data=data
		self.k=k
		self.metric=metric

		if self.metric=='pearson':
			self.fn=self.pearson

	def pearson(self,rating1,rating2):
		xy=0
		sumX=0
		sumY=0
		sqr_X=0
		sqr_Y=0
		n=0

		for key in rating1:
			if key in rating2:
				xy+=rating1[key]*rating2[key]
				sumX+=rating1[key]
				sumY+=rating2[key]
				sqr_X+=rating1[key]**2
				sqr_Y+=rating2[key]**2
				n+=1
		denominator=math.sqrt(sqr_X-sumX**2/float(n))*math.sqrt(sqr_Y-sumY**2/float(n))
		# not capture the denominator is zero !
		if denominator==0:
			return 0
		else:
			return (xy-sumX*sumY/float(n))/float(denominator)

	def computeNeighbour(self,username):
		distance=[]
		for key in self.data:
			if key!=username:
				d=self.fn(self.data[username],self.data[key])
				distance.append((key,d))

		return sorted(distance,key=lambda x:x[1],reverse=True)

	def recommand(self,user):
		distances=self.computeNeighbour(user)
		total=0
		pearson_val=[]
		for i in range(self.k):
			name=distances[i][0]
			pearson_val.append([name,distances[i][1]])
		total=pearson_val.sum()
		# pearson_val=pearson_val
		persons=[]
		for per in pearson_val:
			percent=per[1]/float(total)
			persons.append((per[0],percent))



def main():
	with open('user.json','r') as f:
		users=json.load(f)
	obj=recommander(data=users)
	print obj.computeNeighbour('Chan')

if __name__ == '__main__':
	main()