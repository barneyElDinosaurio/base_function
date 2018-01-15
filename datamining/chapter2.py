#-*-coding=utf-8-*-
import json
#load data
with open('user.json','r') as f:
	user=json.load(f)

# print user
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
	print recommands
	return sorted(recommands,key=lambda x:x.values() ,reverse=True)


# print MinkovskiDistance(user,'Angelica','Veronica',2)
print computeNeighbor('Bill',user,2)