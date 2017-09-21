# coding: utf-8
import json


def getheader():
    with open('request_header') as fp:
        data = fp.readlines()
    dictionary = dict()
    for line in data:
        line = line.strip()
        dictionary[line.split(":")[0]] = ':'.join(line.split(":")[1:])
    return dictionary


def analysis_cookie():
    cookie = getheader()['Cookie']
    for item in items:
        name = item.split('=')[0]
        value = item.split('=')[1]
        print name, " : ", value


def urlParse():
    url = 'https://mbrowser.baidu.com/api/mtoutiao/channel/list?func=query_history&params={%22sid%22:%22TT|zonghe%22,%22version%22:1,%22index%22:9998,%22num%22:20,%22refresh_state%22:202}&ua=I4L08_PSvhgHP2iS45mKot5cmYIGJXuSokWKtgaQXaogus8zouL4ioa_vN_tuXi6UkfAA&cuid=liHo8gahHi02aHi6Y8Sa80af2ig6iS8NgO25a082viiaa283gavW8_aR28_quBtqA&cfrom=1008621m&from=1008621m&crp=0&it=0&ctv=2&st=00000000&nw=wifi&city=340_%E5%8D%97%E5%B1%B1%E5%8C%BA&cen=ua_cuid&count=81&lasttime=1505818887888'
    x = url.split('&')
    fp = open('urlparse', 'a')
    for i in x:
        print i
        fp.write(i + '\n')

    fp.close()

def read_json():
    fp=open('temp','r').read().strip()
    #js=json.load(fp,encoding='utf-8')

    #print fp
    #js=json.loads(fp)
    #print js
    return_data=eval(fp)
    print return_data
    #print return_data['log_extra']
    if return_data.has_key('app_name'):
        print return_data.get('app_name')
        print return_data.get('title')
        print return_data.get('image')
        print return_data.get('image').get('url')
        print "DDD"

    for k,v in return_data.items():
        print k,v
        if k=='filter_words':
            for i in v:
                for k1,v1 in i.items():
                    print k1,v1

if __name__ == "__main__":
    #print getheader()
    # analysis_cookie()
    #urlParse()
    read_json()
