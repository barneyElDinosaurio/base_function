import struct,os
data_path=os.path.join(os.getcwd(),'data')
os.chdir(data_path)
def csv_case():
	mask='5s11s1s'
	with open('dingkuan_data.txt','r') as f:
		for line in f:
			# print line
			fields=struct.Struct(mask).unpack_from(line)
			print fields
			print '*'*10


import numpy as np
import pylab as p
import scipy.signal as signal

def clear_other():
	# get some linear data
	x = np.linspace (0, 1, 101)

	# add some noisy signal
	x[3::10] = 1.5

	p.plot(x)
	p.plot(signal.medfilt(x,3))
	p.plot(signal.medfilt(x,5))

	p.legend(['original signal', 'length 3','length 5'])
	p.show ()

# def clear_mad():
import numpy as np
import matplotlib.pyplot as plt

def is_outlier(points, threshold=3.5):
    """
    Returns a boolean array with True if points are outliers and False 
    otherwise.
    
    Data points with a modified z-score greater than this 
    # value will be classified as outliers.
    """
    # transform into vector
    if len(points.shape) == 1:
        points = points[:,None]

    # compute median value    
    median = np.median(points, axis=0)
    print 'median',median
    # compute diff sums along the axis
    # print 'point',points
    print len(points)
    diff = np.sum((points - median)**2, axis=-1)
    print len(diff)
    diff = np.sqrt(diff)
    # compute MAD
    med_abs_deviation = np.median(diff)
    
    # compute modified Z-score
    # http://www.itl.nist.gov/div898/handbook/eda/section4/eda43.htm#Iglewicz
    modified_z_score = 0.6745 * diff / med_abs_deviation

    # return a mask for each outlier
    return modified_z_score > threshold

def random_mad():
	# Random data
	x = np.random.random(100)

	# histogram buckets
	buckets = 50

	# Add in a few outliers
	x = np.r_[x, -49, 95, 100, -100]

	# Keep inlier data points
	# Note here that 
	# "~" is logical NOT on boolean numpy arrays
	filtered = x[~is_outlier(x)]

	# plot histograms
	plt.figure()

	plt.subplot(211)
	plt.hist(x, buckets)
	plt.xlabel('Raw')

	plt.subplot(212)
	plt.hist(filtered, buckets)
	plt.xlabel('Cleaned')

	plt.show()


def lena_show():
	import scipy.misc
	lena=scipy.misc.ascent()
	plt.gray()
	plt.imshow(lena)
	plt.colorbar()
	# plt.show()
	print lena.shape
	print lena.max()
	print lena.dtype

def other_show():
	import Image
	bug=Image.open('stinkbug.png')
	# arr=np.array(bug.getdata())
	# print arr
	arr=np.array(bug.getdata(),np.uint8).reshape(bug.size[1],bug.size[0],3)
	print arr
	print arr.shape
	print bug.size
	plt.gray()
	plt.imshow(arr)
	plt.colorbar()
	plt.show()

def image_operation():
	import Image

	im=Image.open('stinkbug.png')
	im=im.rotate(90)
	im.show(im)
	# plt.show()

# clear_other()
# lena_show()
# other_show()
image_operation()