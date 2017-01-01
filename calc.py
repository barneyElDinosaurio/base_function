
def yield_calc(rate,money):
    return rate*money/365/100

def test1():
    for i in range(1,6):
        rise=(1.1**i-1)*100
        print "%d day's raise is %.2f" %(i,rise)

c=yield_calc(3.65,1000000)
print c