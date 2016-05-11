import collections
s=[("yellow",1),("red",2),("white",3),("black",4),("green",5)]
d=collections.defaultdict(list)
for k,v in s:
    print "k is %s, v is %d" %(k,v)
    #d[k]=v

    d[k].append(v)

print d

print d
for k in d:
    print "k is %s, v is " %k
    print d[k][0]

print "*"*10
s='mississippi'
d=collections.defaultdict(int)
for k in s:
    #print k
    d[k]+=1

print d

print 'I\'m {},{}'.format("hongten","welcome to you")

mydict=collections.defaultdict(list)
s=[("a",[1,2,3,4]),("b",[2,3,4,5]),("c",[3,4,5,6]),("d",[4,5,6,7])]
for k,v in s:
    mydict[k]=v

print mydict