#-*-coding=utf-8-*-
import json,math
#load data
with open('user.json','r') as f:
	user=json.load(f)

# print(user)
def MinkovskiDistance(user,nameX,nameY,r):
	total=0
	for k,v in user[nameX].items():
		if k in user[nameY]:
			total+=pow(abs(v-user[nameY][k]),r)
	return pow(total,1.0/2)

def computeNeighbor(username,user,r):
	recommands=[]
	for k in user:
		distance=0
		if k!=username:
			distance=MinkovskiDistance(user,username,k,2)
			recommands.append({k:distance})
	# print(recommands)
	return sorted(recommands,key=lambda x:x.values() ,reverse=True)

def pearson(user1,user2):
	xy=0
	sumX=0
	sumY=0
	sqr_X=0
	sqr_Y=0
	n=0

	for key in user1:
		if key in user2:
			xy+=user1[key]*user2[key]
			sumX+=user1[key]
			sumY+=user2[key]
			sqr_X+=user1[key]**2
			sqr_Y+=user2[key]**2
			n+=1

	# not capture the denominator is zero !
	if math.sqrt(sqr_X-sumX**2/float(n))*math.sqrt(sqr_Y-sumY**2/float(n))==0:
		return 0
	else:
		return (xy-sumX*sumY/float(n))/float(math.sqrt(sqr_X-sumX**2/float(n))*math.sqrt(sqr_Y-sumY**2/float(n)))

# ??? 怎么实现这个
def cosin(user1,user2):
	sumXY=0
	x_len=0
	y_len=0
	for key in user1:
		pass


def main():
	# print(MinkovskiDistance(user,'Angelica','Veronica',2))
	# print(computeNeighbor('Bill',user,2))
	# print(pearson(user['Angelica'],user['Bill']))
	# print(pearson(user['Angelica'],user['Hailey']))
	print(pearson(user['Angelica'],user['Jordyn']))



if __name__ == '__main__':
	main()