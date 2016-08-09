__author__ = 'rocchen'
#-*-coding=utf-8-*-
import urllib2,re,sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getPost(date_time, filter_p):
    url = 'https://zhhrb.sinaapp.com/index.php?date=' + date_time
    user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    header = {"User-Agent": user_agent}
    req = urllib2.Request(url, headers=header)
    resp = urllib2.urlopen(req)
    content = resp.read()
    p = re.compile('<h2 class="question-title">(.*)</h2></br></a>')
    result = re.findall(p, content)
    print result


def get_page():
    user_agent="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    header={"User-Agent":user_agent}
    #url="http://www.qq.com"
    url="http://photo.xitek.com/style/0/p/1"
    req = urllib2.Request(url,headers=header)
    result = urllib2.urlopen(req).read()
    print result
    #p = re.compile(r'<a class='\blast\' href=\'/style/0/p/(\d+)' >')
    #p = re.compile('target="(.*)"')
    #p = re.compile('<img src="(.*?)" ')
    p = re.compile('<a class=\'blast\' href=\'/style/0/p/(\d+)\' >')
    #<a class='blast' href='/style/0/p/113' >
    page = p.findall(result)
    print type(page)
    print len(page)
    #print page
    '''
    if page:
        print page[0]
        return page[0]
        # print page[0]
        #return page[0]
    '''
    print "return"
    for i in page:
        print i
get_page()
urllib2.url
#filter_p = re.compile('����.*')
#getPost('20160620',filter_p)