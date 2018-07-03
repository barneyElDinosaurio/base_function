import os
import re
import sys
try:
    from PIL import Image
except Exception as e:
    import Image

def low_image():
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

def low_snapshot(filename):
    im = Image.open(filename)
    w,h = im.size

    new_im = im.resize((w*3.0/5,h*3.0/5),Image.ANTIALIAS)
    name = filename.split('.')[0]
    post_fix = filename.split('.')[1]
    new_name = name+'_thunbnail.'+post_fix
    new_im.save(new_name)    


def low_down(filename):
    im = Image.open(filename)
    w,h = im.size
    if w>1000 or h >1000:
        new_im = im.resize((w/2,h/2),Image.ANTIALIAS)
        name = filename.split('.')[0]
        post_fix = filename.split('.')[1]
        new_name = name+'_thunbnail.'+post_fix
        new_im.save(new_name)


if __name__=='__main__':
    if len(sys.argv)>1:
        filename=sys.argv[1]
    else:
        filename=''

    print filename
    low_snapshot(filename)
