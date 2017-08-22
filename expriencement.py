#-*-coding=utf-8-*-
'''
抓取搜狐客户端的广告主
'''
import datetime
import random
import xlwt
import requests
import time
from pandas.io.json import json_normalize
import pandas as pd
import json
class sohu_cls():
    def __init__(self):
        self.headers={'Host': 'api.k.sohu.com','User-Agent': 'SohuNews/5.9.3 BuildCode/126',
                      'Authorization': '990006203070023','Content-Encoding': 'UTF-8'}
        self.new_url='http://api.k.sohu.com/api/channel/v6/news.go?p1=NjMwMjg4NTczMDc1OTEyNzA2OA%3D%3D&pid=-1&channelId=1&num=20&imgTag=1&showPic=1&picScale=11&rt=json&net=wifi&cdma_lat=22.553053&cdma_lng=113.902393&from=channel&mac=b4%3A0b%3A44%3A83%3A93%3A16&AndroidID=4dd00e258bbe295f&carrier=CMCC&imei=990006203070023&imsi=460020242631842&density=3.0&apiVersion=37&skd=9bf84c6c9d24711f43f7058db2d1ed5ba7c6a2fecca504d3f44839a8bf22b4521ff192a4ac2d77946d871706ceb89baa269d145d2f5a07fddb656d6417029bb04459d2a5aa0ca50764b2de62da32f9e5e6055efa78b93cafbd89ef0971a836d3542ce2065edff7017a28b164e4210fec&v=1502985600&t=1503044087&page=1&action=0&mode=0&cursor=0&mainFocalId=0&focusPosition=1&viceFocalId=0&lastUpdateTime=0&gbcode=440300&forceRefresh=0&apiVersion=37&u=1&source=0&isSupportRedPacket=0&t=1503044087'


        self.old_url='http://api.k.sohu.com/api/channel/v6/news.go?p1=NjMwMjg4NTczMDc1OTEyNzA2OA%3D%3D&pid=-1&channelId=1&num=20&imgTag=1&showPic=1&picScale=11&rt=json&net=wifi&cdma_lat=22.568970&cdma_lng=113.948697&from=channel&mac=b4%3A0b%3A44%3A83%3A93%3A16&AndroidID=4dd00e258bbe295f&carrier=CMCC&imei=990006203070023&imsi=460020242631842&density=3.0&apiVersion=37&skd=9bf84c6c9d24711f43f7058db2d1ed5ba7c6a2fecca504d3f44839a8bf22b4521ff192a4ac2d77946d871706ceb89baa26d2a04c74e7f9a802366235a8d013a24459d2a5aa0ca50764b2de62da32f9e5e6055efa78b93cafbd89ef0971a836d3542ce2065edff7017a28b164e4210fec&v=1502985600&t=1502992147&page=2&action=2&mode=1&cursor=6817205&mainFocalId=6816008&focusPosition=2&viceFocalId=0&lastUpdateTime=0&gbcode=440300&forceRefresh=0&apiVersion=37&u=1&source=0&isSupportRedPacket=0&t=1502992147'

        self.current=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%M')+'.xls'
        self.excelFile=xlwt.Workbook()

        self.sheet=self.excelFile.add_sheet('sohu')
        self.row = 0

    def stamptolocaltime(self,stamp):
        #10bit
        return datetime.datetime.fromtimestamp(stamp)

    def localtimetostamp(self,t):
        pass

    def getData(self,ids,page,row_args):
        #url=self.header_fill('page2.cfg',ids,page)
        url='http://api.k.sohu.com/api/channel/v5/news.go?p1=NjMwMjg4NTczMDc1OTEyNzA2OA%3D%3D&pid=-1&channelId=3&num=20&imgTag=1&showPic=1&picScale=11&rt=json&net=wifi&cdma_lat=22.553063&cdma_lng=113.902367&from=channel&mac=b4%3A0b%3A44%3A83%3A93%3A16&AndroidID=4dd00e258bbe295f&carrier=CMCC&imei=990006203070023&imsi=460020242631842&density=3.0&apiVersion=37&skd=181cd7756f3346031f3c2cabb5747dbf9592f0ba9027bcbc4e8428628dee61e63c6043ce4d6b2df978eedd56c6ac5d70783755af90a01e6e2d50b9c0bf976aef41762bf8129a2be6ec278d9f5b07b347b8619ff25e017fcb26fdc0bd0a6529493310b14ea6ae9d195d6d19f662ee9ad1&v=1503331200&t=1503382594&page=2&action=2&mode=1&cursor=6836395&mainFocalId=0&focusPosition=2&viceFocalId=0&lastUpdateTime=0&gbcode=440300&apiVersion=37&u=1&isSupportRedPacket=0&t=1503382594'
        print url
        row=row_args
        try:
            s=requests.get(url,headers=self.headers)
            print s.status_code
        except Exception,e:
            print "requests issue"
            return 'error'
        js= s.json()
        #print json_normalize(js)
        #self.jsonParse(js)
        #time.sleep(50)
        articles=js[u'articles']
        #print articles

        '''
        #self.save2file('sohu_key.cfg',js.keys(),'w')
        dateFormat = xlwt.XFStyle()
        dateFormat.num_format_str = 'yyyy/mm/dd'
        #for article in article:
        '''
        for article in articles:
            if article['newsType']==21:
                print 'row :',row
                col = 0
                newsIds=article['newsId']
                '''
                print newsIds
                self.sheet.write(row,col,newsIds)
                col=col+1
                '''
                #df=pd.DataFrame(article)
                #print df
                #df.to_excel(str(newsIds)+'.xls',encoding='utf-8')
                #print len(df)

                for k,v in article.items():
                    #print k,type(k)
                    if k==u'link':
                        #self.sheet.write(row, col, v)
                        col = col + 1

                    if k==u'data':
                        #df2=pd.DataFrame(v,index=range(len(v)))
                        #如果需要这个字段，取消注释
                        #df2.to_excel(str(newsIds)+'_data.xls',encoding='utf-8')

                        if v.has_key('online'):
                            on_line_timestamp=article[k]['online']
                            off_line_timestamp=article[k]['offline']
                            if type(on_line_timestamp) !=type(1):
                                on_line_timestamp=int(on_line_timestamp)
                                off_line_timestamp=int(off_line_timestamp)
                            #self.sheet.write(row,col,self.stamptolocaltime(on_line_timestamp),dateFormat)
                            col = col + 1
                            #self.sheet.write(row,col,self.stamptolocaltime(off_line_timestamp),dateFormat)
                            col = col + 1

                        if v.has_key('link'):
                            link=article[k]['link']
                            self.sheet.write(row,col,link)
                            col=col+1
                        if v.has_key('resource'):
                            if v['resource'].has_key('adcode'):
                                adcode=v['resource']['adcode']
                                self.sheet.write(row, col, adcode)
                                col = col + 1
                            if v['resource'].has_key('text'):
                                text=v['resource']['text']
                                self.sheet.write(row, col, text)
                                col = col + 1
                            if v['resource'].has_key('click'):
                                click=v['resource']['click']
                                self.sheet.write(row, col, click)
                                col = col + 1
                            if v['resource'].has_key('click'):
                                click=v['resource']['click']
                                self.sheet.write(row, col, click)
                                col = col + 1
                        if v.has_key('resource1'):
                            if v['resource1'].has_key('adcode'):
                                adcode=v['resource1']['adcode']
                                self.sheet.write(row, col, adcode)
                                col = col + 1
                            if v['resource1'].has_key('text'):
                                text=v['resource1']['text']
                                self.sheet.write(row, col, text)
                                col = col + 1
                            if v['resource1'].has_key('click'):
                                click=v['resource1']['click']
                                self.sheet.write(row, col, click)
                                col = col + 1
                            if v['resource1'].has_key('click'):
                                click=v['resource1']['click']
                                self.sheet.write(row, col, click)
                                col = col + 1
                        if v.has_key('resource2'):
                            if v['resource2'].has_key('adcode'):
                                adcode=v['resource2']['adcode']
                                self.sheet.write(row, col, adcode)
                                col = col + 1
                            if v['resource2'].has_key('text'):
                                text=v['resource2']['text']
                                self.sheet.write(row, col, text)
                                col = col + 1
                            if v['resource2'].has_key('click'):
                                click=v['resource2']['click']
                                self.sheet.write(row, col, click)
                                col = col + 1
                            if v['resource'].has_key('click'):
                                click=v['resource']['click']
                                self.sheet.write(row, col, click)
                                col = col + 1
                        if v.has_key('resource3'):
                            if v['resource3'].has_key('adcode'):
                                adcode=v['resource3']['adcode']
                                self.sheet.write(row, col, adcode)
                                col = col + 1
                            if v['resource3'].has_key('text'):
                                text=v['resource3']['text']
                                self.sheet.write(row, col, text)
                                col = col + 1
                            if v['resource3'].has_key('click'):
                                click=v['resource3']['click']
                                self.sheet.write(row, col, click)
                                col = col + 1
                            if v['resource3'].has_key('click'):
                                click=v['resource3']['click']
                                self.sheet.write(row, col, click)
                                col = col + 1
                        if v.has_key('resource4'):
                            if v['resource4'].has_key('adcode'):
                                adcode=v['resource4']['adcode']
                                self.sheet.write(row, col, adcode)
                                col = col + 1
                            if v['resource4'].has_key('text'):
                                text=v['resource4']['text']
                                self.sheet.write(row, col, text)
                                col = col + 1
                            if v['resource4'].has_key('click'):
                                click=v['resource4']['click']
                                self.sheet.write(row, col, click)
                                col = col + 1
                            if v['resource4'].has_key('click'):
                                click=v['resource4']['click']
                                self.sheet.write(row, col, click)
                                col = col + 1
                        if v.has_key('resource5'):
                            if v['resource5'].has_key('adcode'):
                                adcode=v['resource5']['adcode']
                                self.sheet.write(row, col, adcode)
                                col = col + 1
                            if v['resource5'].has_key('text'):
                                text=v['resource5']['text']
                                self.sheet.write(row, col, text)
                                col = col + 1
                            if v['resource5'].has_key('click'):
                                click=v['resource5']['click']
                                self.sheet.write(row, col, click)
                                col = col + 1
                            if v['resource5'].has_key('click'):
                                click=v['resource5']['click']
                                self.sheet.write(row, col, click)
                                col = col + 1
                        if v.has_key('resource6'):
                            if v['resource6'].has_key('adcode'):
                                adcode=v['resource6']['adcode']
                                self.sheet.write(row, col, adcode)
                                col = col + 1
                            if v['resource6'].has_key('text'):
                                text=v['resource6']['text']
                                self.sheet.write(row, col, text)
                                col = col + 1
                            if v['resource6'].has_key('click'):
                                click=v['resource6']['click']
                                self.sheet.write(row, col, click)
                                col = col + 1
                            if v['resource6'].has_key('click'):
                                click=v['resource6']['click']
                                self.sheet.write(row, col, click)
                                col = col + 1
                        if v.has_key('resource7'):
                            if v['resource7'].has_key('adcode'):
                                adcode=v['resource7']['adcode']
                                self.sheet.write(row, col, adcode)
                                col = col + 1
                            if v['resource7'].has_key('text'):
                                text=v['resource7']['text']
                                self.sheet.write(row, col, text)
                                col = col + 1
                            if v['resource7'].has_key('click'):
                                click=v['resource7']['click']
                                self.sheet.write(row, col, click)
                                col = col + 1
                            if v['resource7'].has_key('click'):
                                click=v['resource7']['click']
                                self.sheet.write(row, col, click)
                                col = col + 1
                        if v.has_key('resource8'):
                            if v['resource8'].has_key('adcode'):
                                adcode=v['resource8']['adcode']
                                self.sheet.write(row, col, adcode)
                                col = col + 1
                            if v['resource8'].has_key('text'):
                                text=v['resource8']['text']
                                self.sheet.write(row, col, text)
                                col = col + 1
                            if v['resource8'].has_key('click'):
                                click=v['resource8']['click']
                                self.sheet.write(row, col, click)
                                col = col + 1
                            if v['resource8'].has_key('click'):
                                click=v['resource8']['click']
                                self.sheet.write(row, col, click)
                                col = col + 1

                row = row + 1
        self.excelFile.save(self.current)
        return row

    def getChannelID(self):
        url=self.header_fill('argsv7.cfg',0,0)
        print url
        s=requests.get(url=url,headers=self.headers)
        js=s.json()
        #print js['data']
        result=[]

        for item in js['data']:
            for ids in item['channelList']:
                if ids.has_key('id'):
                    result.append(ids['id'])

        return result

    def urlParse(self):
        #new_url='http://api.k.sohu.com/api/channel/v6/news.go?p1=NjMwMjg4NTczMDc1OTEyNzA2OA%3D%3D&pid=-1&channelId=1&num=20&imgTag=1&showPic=1&picScale=11&rt=json&net=wifi&cdma_lat=22.553053&cdma_lng=113.902393&from=channel&mac=b4%3A0b%3A44%3A83%3A93%3A16&AndroidID=4dd00e258bbe295f&carrier=CMCC&imei=990006203070023&imsi=460020242631842&density=3.0&apiVersion=37&skd=9bf84c6c9d24711f43f7058db2d1ed5ba7c6a2fecca504d3f44839a8bf22b4521ff192a4ac2d77946d871706ceb89baa269d145d2f5a07fddb656d6417029bb04459d2a5aa0ca50764b2de62da32f9e5e6055efa78b93cafbd89ef0971a836d3542ce2065edff7017a28b164e4210fec&v=1502985600&t=1503044087&page=1&action=0&mode=0&cursor=0&mainFocalId=0&focusPosition=1&viceFocalId=0&lastUpdateTime=0&gbcode=440300&forceRefresh=0&apiVersion=37&u=1&source=0&isSupportRedPacket=0&t=1503044087'
        url1='http://api.k.sohu.com/api/channel/v6/news.go?p1=NjMwMjg4NTczMDc1OTEyNzA2OA%3D%3D&pid=-1&channelId=13557&num=20&imgTag=1&showPic=1&picScale=11&rt=json&net=wifi&cdma_lat=22.553062&cdma_lng=113.902395&from=channel&mac=b4%3A0b%3A44%3A83%3A93%3A16&AndroidID=4dd00e258bbe295f&carrier=CMCC&imei=990006203070023&imsi=460020242631842&density=3.0&apiVersion=37&skd=9bf84c6c9d24711f43f7058db2d1ed5ba7c6a2fecca504d3f44839a8bf22b4521ff192a4ac2d77946d871706ceb89baa7f1d447f8316658817b98665249284124459d2a5aa0ca50764b2de62da32f9e5e6055efa78b93cafbd89ef0971a836d3542ce2065edff7017a28b164e4210fec&v=1502985600&t=1503048481&page=2&action=2&mode=3&cursor=0&mainFocalId=0&focusPosition=0&viceFocalId=0&lastUpdateTime=0&contentToken=no_data&gbcode=440300&forceRefresh=0&apiVersion=37&u=1&source=0&isSupportRedPacket=0&t=1503048481&rr=2'
        url2='http://api.k.sohu.com/api/channel/v6/news.go?p1=NjMwMjg4NTczMDc1OTEyNzA2OA%3D%3D&pid=-1&channelId=13557&num=20&imgTag=1&showPic=1&picScale=11&rt=json&net=wifi&cdma_lat=22.553062&cdma_lng=113.902395&from=channel&mac=b4%3A0b%3A44%3A83%3A93%3A16&AndroidID=4dd00e258bbe295f&carrier=CMCC&imei=990006203070023&imsi=460020242631842&density=3.0&apiVersion=37&skd=9bf84c6c9d24711f43f7058db2d1ed5ba7c6a2fecca504d3f44839a8bf22b4521ff192a4ac2d77946d871706ceb89baaea4e2f0e5c431d0c00935398bb7296c74459d2a5aa0ca50764b2de62da32f9e5e6055efa78b93cafbd89ef0971a836d3542ce2065edff7017a28b164e4210fec&v=1502985600&t=1503048503&page=3&action=2&mode=3&cursor=219062036&mainFocalId=0&focusPosition=0&viceFocalId=0&lastUpdateTime=0&contentToken=no_data&gbcode=440300&forceRefresh=0&apiVersion=37&u=1&source=0&isSupportRedPacket=0&t=1503048503&rr=3 '
        url3='http://api.k.sohu.com/api/channel/v6/news.go?p1=NjMwMjg4NTczMDc1OTEyNzA2OA%3D%3D&pid=-1&channelId=13557&num=20&imgTag=1&showPic=1&picScale=11&rt=json&net=wifi&cdma_lat=22.553062&cdma_lng=113.902395&from=channel&mac=b4%3A0b%3A44%3A83%3A93%3A16&AndroidID=4dd00e258bbe295f&carrier=CMCC&imei=990006203070023&imsi=460020242631842&density=3.0&apiVersion=37&skd=9bf84c6c9d24711f43f7058db2d1ed5ba7c6a2fecca504d3f44839a8bf22b4521ff192a4ac2d77946d871706ceb89baacb8993c8c99aaaa285ed6772c5e4f25a4459d2a5aa0ca50764b2de62da32f9e5e6055efa78b93cafbd89ef0971a836d3542ce2065edff7017a28b164e4210fec&v=1502985600&t=1503048528&page=4&action=2&mode=3&cursor=219108135&mainFocalId=0&focusPosition=0&viceFocalId=0&lastUpdateTime=0&contentToken=no_data&gbcode=440300&forceRefresh=0&apiVersion=37&u=1&source=0&isSupportRedPacket=0&t=1503048528&rr=4'
        url4='http://api.k.sohu.com/api/channel/v7/list.go?rt=xml&supportLive=1&supportWeibo=1&v=5.9.3&cdma_lng=114.040749&cdma_lat=22.968338&up=1,13557,283,3,247,6,4,5,23,2,45,960415,11,351,279,12,954509,98,50,16,177,248,49,359980,46,250,960377,25&down=&local=283&change=0&isStartUp=1&p1=NjMwMjg4NTczMDc1OTEyNzA2OA%3D%3D&gid=02ffff110611113d8198de0286beef8b42dff620a1c511&pid=-1&apiVersion=37'
        url5='http://api.k.sohu.com/api/channel/v7/list.go?rt=xml&supportLive=1&supportWeibo=1&v=5.9.3&cdma_lng=114.040795&cdma_lat=22.968323&up=1,13557,283,3,247,6,4,5,23,2,45,960415,11,351,279,12,954509,98,50,16,177,248,49,359980,46,250,960377,25&down=&local=283&change=0&isStartUp=1&p1=NjMwMjg4NTczMDc1OTEyNzA2OA%3D%3D&gid=02ffff110611113d8198de0286beef8b42dff620a1c511&pid=-1&apiVersion=37'
        url6='http://api.k.sohu.com/api/channel/v5/news.go?p1=NjMwMjg4NTczMDc1OTEyNzA2OA%3D%3D&pid=-1&channelId=3&num=20&imgTag=1&showPic=1&picScale=11&rt=json&net=wifi&cdma_lat=22.968338&cdma_lng=114.040749&from=channel&mac=b4%3A0b%3A44%3A83%3A93%3A16&AndroidID=4dd00e258bbe295f&carrier=CMCC&imei=990006203070023&imsi=460020242631842&density=3.0&apiVersion=37&skd=0dc0b070b814cb273b23f2a8c8ae111eb512517ae95e6dfb4e9259e269b66521df8a901146721a9e2cffe0f3edd41978944803e2cc9db3acfc451a6e76a714a4a72259c46244969f343c3be0857f6bb0407d398aad82b4f325ce836a32fb9d4d2bde56d44ed1ba3d859020fa53d19c7e&v=1503072000&t=1503126526&page=1&action=0&mode=0&cursor=0&mainFocalId=0&focusPosition=1&viceFocalId=0&lastUpdateTime=0&gbcode=441900&apiVersion=37&u=1&isSupportRedPacket=0&t=1503126526 '
        url7='http://api.k.sohu.com/api/channel/v6/news.go?p1=NjMwMjg4NTczMDc1OTEyNzA2OA%3D%3D&pid=-1&channelId=1&num=20&imgTag=1&showPic=1&picScale=11&rt=json&net=wifi&cdma_lat=22.968338&cdma_lng=114.040749&from=channel&mac=b4%3A0b%3A44%3A83%3A93%3A16&AndroidID=4dd00e258bbe295f&carrier=CMCC&imei=990006203070023&imsi=460020242631842&density=3.0&apiVersion=37&skd=0dc0b070b814cb273b23f2a8c8ae111eb512517ae95e6dfb4e9259e269b66521df8a901146721a9e2cffe0f3edd4197826eceede9c035946595d7a369e659fbfa72259c46244969f343c3be0857f6bb0407d398aad82b4f325ce836a32fb9d4d2bde56d44ed1ba3d859020fa53d19c7e&v=1503072000&t=1503126463&page=1&action=0&mode=0&cursor=0&mainFocalId=0&focusPosition=1&viceFocalId=0&lastUpdateTime=0&gbcode=441900&forceRefresh=0&apiVersion=37&u=1&source=0&isSupportRedPacket=0&t=1503126463'
        url8='http://api.k.sohu.com/api/channel/v5/news.go?p1=NjMwMjg4NTczMDc1OTEyNzA2OA%3D%3D&pid=-1&channelId=3&num=20&imgTag=1&showPic=1&picScale=11&rt=json&net=wifi&cdma_lat=22.553056&cdma_lng=113.902387&from=channel&mac=b4%3A0b%3A44%3A83%3A93%3A16&AndroidID=4dd00e258bbe295f&carrier=CMCC&imei=990006203070023&imsi=460020242631842&density=3.0&apiVersion=37&skd=181cd7756f3346031f3c2cabb5747dbf9592f0ba9027bcbc4e8428628dee61e63c6043ce4d6b2df978eedd56c6ac5d701d090c77a3cb20001501b428fdb59b9f41762bf8129a2be6ec278d9f5b07b347b8619ff25e017fcb26fdc0bd0a6529493310b14ea6ae9d195d6d19f662ee9ad1&v=1503331200&t=1503382173&page=1&action=0&mode=0&cursor=0&mainFocalId=0&focusPosition=1&viceFocalId=0&lastUpdateTime=0&gbcode=440300&apiVersion=37&u=1&isSupportRedPacket=0&t=1503382173'
        url9='http://api.k.sohu.com/api/channel/v5/news.go?p1=NjMwMjg4NTczMDc1OTEyNzA2OA%3D%3D&pid=-1&channelId=3&num=20&imgTag=1&showPic=1&picScale=11&rt=json&net=wifi&cdma_lat=22.553063&cdma_lng=113.902367&from=channel&mac=b4%3A0b%3A44%3A83%3A93%3A16&AndroidID=4dd00e258bbe295f&carrier=CMCC&imei=990006203070023&imsi=460020242631842&density=3.0&apiVersion=37&skd=181cd7756f3346031f3c2cabb5747dbf9592f0ba9027bcbc4e8428628dee61e63c6043ce4d6b2df978eedd56c6ac5d70783755af90a01e6e2d50b9c0bf976aef41762bf8129a2be6ec278d9f5b07b347b8619ff25e017fcb26fdc0bd0a6529493310b14ea6ae9d195d6d19f662ee9ad1&v=1503331200&t=1503382594&page=2&action=2&mode=1&cursor=6836395&mainFocalId=0&focusPosition=2&viceFocalId=0&lastUpdateTime=0&gbcode=440300&apiVersion=37&u=1&isSupportRedPacket=0&t=1503382594'
        x=url9.split('&')
        fp=open('page2.cfg','w')

        for i in x:
            print i
            fp.write(i+'\n')

        fp.close()

    def save2file(self,filename,content,t):
        with open(filename,t) as fp:
            [fp.write(i+'\n') for i in content]

    def jsonParse(self,dictionary):
        with open('channelID.txt','r') as fp:
            str_data=fp.read().strip()
        #print str_data
        #dictionary=json.loads(str_data)
        dictionary=eval(str_data)
        print type(dictionary)
        print dictionary
        input('')
        if isinstance(dictionary,dict):
            for i in range(len(dictionary)):
                key=dictionary.keys()[i]
                value=dictionary[key]
                print key,value
                self.jsonParse(value)
            print '\n'

    def header_fill(self,filename,ids,page):
        #url=''
        t=int(time.time())
        with open(filename,'r') as fp:
            line=fp.readline().strip()
            url=line
            #print url
            curr_d = datetime.datetime.fromtimestamp(t)
            while 1:
                #print url
                line = fp.readline().strip()
                if len(line)<1:
                    break
                sp=line.split('=')
                #print sp[0],sp[1]
                #print arg,val
                if sp[0]=='channelId':
                    url=url+'&'+'channelId='+ids
                if sp[0]=='page':
                    url=url+'&'+'page='+page
                elif sp[0]=='t':
                    url=url+'&'+str(t)
                else:
                    url=url+'&'+line
                #print 'done'
        return url
        #print url

    def fetchAll(self,pages):
        id_list=self.getChannelID()
        row=0
        for ids in id_list:
            print "channel ID" , ids
            for page in range(pages):
                print 'outside row ',row
                row=self.getData(str(ids),str(page),row)
                #time.sleep(random.random()*5)
                #self.row=self.row+1
                if row=='error':
                    self.excelFile.save(self.current)

        self.excelFile.save(self.current)

    def drop_dup(self):
        filename=self.current
        df=pd.read_excel(filename)
        df=df.drop_duplicates()
        df.to_excel('new_sohu.xls')



def main():
    print 'Stsrt :', datetime.datetime.now()
    print 'timestamp :', time.time()
    obj=sohu_cls()
    #obj.urlParse()
    #obj.fetchAll(20)
    obj.getData('3','2',0)
    print 'End :',datetime.datetime.now()
    print 'timestamp :', time.time()
main()