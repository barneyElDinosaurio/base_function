__author__ = 'rocky'
import urllib2,StringIO,gzip

url = "http://photo.xitek.com/style/0/p/10"
user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
headers = {"User-Agent": user_agent}
req = urllib2.Request(url, headers=headers)
resp = urllib2.urlopen(req)
content = resp.read()
code = resp.info().get("Content-Encoding")
print code
if code == None:
    print "No gzip"
    print content
else:
    print "gzip"
    # print content
    data = StringIO.StringIO(content)
    gzipper = gzip.GzipFile(fileobj=data)
    html = gzipper.read()
    print html
    #content = resp.read()
    #print content