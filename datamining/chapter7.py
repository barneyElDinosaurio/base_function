#-*-coding=utf-8-*-
from PIL import Image
import requests
from lxml import etree
from io import BytesIO
import pytesseract


def download(url,retry=3):
	try:
		r=requests.get(url=url)
	except Exception as e:
		print e
		if retry <0:
			return None
		else:
			download(url,retry-1)
	return r.text

def getCaptcha():
	url='http://example.webscraping.com/places/default/user/register?_next=/places/default/index'
	text=download(url)
	if text:
		tree=etree.HTML(text)
		print tree
		im_data=tree.xpath('//div[@id="recaptcha"]/img/@src')[0]
		im_data=im_data.split(',')[-1]
		binary_img_data=im_data.decode('base64')
		file_like = BytesIO(binary_img_data)
		im=Image.open(file_like)
		# im.show()
		# im.save('code.png')
		return im

	else:
		return None

def recognize_captcha():
	im=getCaptcha()
	
	code=pytesseract.image_to_string(im)
	print code

def main():
	recognize_captcha()

if __name__ == '__main__':
	main()