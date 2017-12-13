import os
import re
from PIL import Image
current_path = os.getcwd()
for i in os.listdir(current_path):
    if re.search('\.jpg|\.png',i) and not re.search('_thunbnail',i):
        print i.decode('gbk')
        im = Image.open(os.path.join(current_path,i))
        w,h = im.size
        if w>1000 or h >1000:
            new_im = im.resize((w/4,h/4),Image.ANTIALIAS)
            name = i.split('.')[0]
            post_fix = i.split('.')[1]
            new_name = os.path.join(current_path,name+'_thunbnail.'+post_fix)
            new_im.save(new_name)
