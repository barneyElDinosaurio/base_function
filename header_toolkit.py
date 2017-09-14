# coding: utf-8

def getheader():
    with open('request_header') as fp:
        data=fp.readlines()
    dictionary=dict()
    for line in data:
        line=line.strip()
        dictionary[line.split(":")[0]]=':'.join(line.split(":")[1:])
    return dictionary

def analysis_cookie():
    cookie=getheader()['Cookie']
    items=cookie.split(';')
    for item in items:
        name=item.split('=')[0]
        value=item.split('=')[1]
        print name," : ",value

if __name__=="__main__":
    print getheader()
    #analysis_cookie()