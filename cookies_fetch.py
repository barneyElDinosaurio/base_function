# -*-coding=utf-8-*-
__author__ = 'Rocky'
import requests


def csdn():
    session = requests.session()
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'}
    url = 'http://msg.csdn.net/'
    header[
        'Cookie'] = 'uuid_tt_dd=-5697318013068753627_20160111; _ga=GA1.2.795042232.1452766190; _message_m=quvq2wle24wa4aweppwic204; UserName=yagamil; UserInfo=zMhiNgesgIlEBQ3TOqLCtx4nUI360IIq3ciBzg4EKH%2FW8mSpTANpu5cTlRFLj2Tqh%2FZzQr2rNqDtT1SZz%2Be2%2FpDkGoQxDK3IVUZXvwZ%2FEP1I4UTg6MoZkH7LDO3sjrJJ; UserNick=%E9%87%8D%E5%A4%8D%E7%9A%84%E7%94%9F%E6%B4%BB; AU=0F1; UD=%E8%AE%B0%E5%BD%95%E8%87%AA%E5%AD%A6%E7%9A%84%E5%8E%86%E7%A8%8B+%E5%88%83%E8%8D%89+www.rcdisk.com; UN=yagamil; UE="chen_jinwei@126.com"; BT=1490707396344; access-token=c2e12bff-5b27-4a91-953b-448ff6f6beac; _csdn_notify_admin_session=VE41a0d3TitrVGY2bGtXY09pZENwR1lHenhUU1NVaWc1b04wL1I3dCtDQVdadWpjMXBzdGRJL0RZR04wYldvZDBhTU96b2oycVVKeVI1UEVyUHFKbG1yNnB2b2pHRWVnWG1uc2JMM2R3YWthakRyTXZNaEpVU1NtUy9zQUJrNjd3R2lpbG5PK0paMnlyc1dyK0lTZUtRPT0tLXlPQUE1QzF5UmhDNjEvSFdtRFlQS2c9PQ%3D%3D--4569c5a32916dcf969a8b7e007c37abeb90be4f3; dc_tos=onj1dg; dc_session_id=1490707393375; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1490024083,1490024559,1490374375,1490707368; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1490707638'
    header['Cache-Control'] = 'max-age=0'
    header['Host'] = 'msg.csdn.net'
    header['Referer'] = 'http://blog.csdn.net/yagamil'
    resp = requests.get(url, headers=header)
    # resp=session.get(url,headers=header)
    print resp.text


def getFromWebBrowser():
    #not work
    import requests
    import browsercookie
    cj = browsercookie.chrome()
    r = requests.get('http://stackoverflow.com', cookies=cj)

#csdn()
#getFromWebBrowser()

import os
import sqlite3
import cookielib
import Cookie
import urllib2

def build_opener_with_chrome_cookies(domain=None):
    #同样失败了
    cookie_file_path = os.path.join(os.environ['LOCALAPPDATA'], r'Google\Chrome\User Data\Default\Cookies')
    if not os.path.exists(cookie_file_path):
        raise Exception('Cookies file not exist!')
    conn = sqlite3.connect(cookie_file_path)
    sql = 'select host_key, name, value, path from cookies'
    if domain:
        sql += ' where host_key like "%{}%"'.format(domain)

    cookiejar = cookielib.CookieJar()    # No cookies stored yet

    for row in conn.execute(sql):
        print row
        cookie_item = cookielib.Cookie(
            version=0, name=row[1], value=row[2],
                     port=None, port_specified=None,
                     domain=row[0], domain_specified=None, domain_initial_dot=None,
                     path=row[3], path_specified=None,
                     secure=None,
                     expires=None,
                     discard=None,
                     comment=None,
                     comment_url=None,
                     rest=None,
                     rfc2109=False,
            )
        cookiejar.set_cookie(cookie_item)    # Apply each cookie_item to cookiejar
    conn.close()
    return urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))    # Return opener

#build_opener_with_chrome_cookies()


class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    #cookie='lj-ss=5bd2bc45dbdf0644d704777dc2075366; lianjia_uuid=c6a7836e-cf96-45ae-96e5-6fdb2def9fb7; UM_distinctid=15e17d9bbf960c-08e33a5d4e4891-4d015463-1fa400-15e17d9bbfa300; select_city=440300; select_nation=1; CNZZDATA1254525948=145009446-1503633660-%7C1503908541; CNZZDATA1253491255=851767322-1503638199-%7C1503907203; _ga=GA1.2.331020171.1503638699; _gid=GA1.2.2040440312.1503909104; _gat=1; _gat_past=1; _gat_new=1; _gat_global=1; _gat_new_global=1; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1503638699; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1503912523; lianjia_ssid=290ce12b-c434-4782-9b1a-06c450c2dbb3'
    #cookie='lj-ss=5bd2bc45dbdf0644d704777dc2075366; lianjia_uuid=c6a7836e-cf96-45ae-96e5-6fdb2def9fb7; UM_distinctid=15e17d9bbf960c-08e33a5d4e4891-4d015463-1fa400-15e17d9bbfa300; select_nation=1; select_city=441900; CNZZDATA1253491255=851767322-1503638199-%7C1503914876; _ga=GA1.2.331020171.1503638699; _gid=GA1.2.2040440312.1503909104; _gat=1; _gat_past=1; _gat_new=1; _gat_global=1; _gat_new_global=1; CNZZDATA1254525948=145009446-1503633660-%7C1503919341; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1503638699; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1503920035; lianjia_ssid=e07f3016-cad2-4f82-96f5-516af563669e'
    #cookie='lj-ss=5bd2bc45dbdf0644d704777dc2075366; lianjia_uuid=c6a7836e-cf96-45ae-96e5-6fdb2def9fb7; UM_distinctid=15e17d9bbf960c-08e33a5d4e4891-4d015463-1fa400-15e17d9bbfa300; select_nation=1; gr_user_id=4571568e-96d5-467c-ad95-9dd1f55471e1; ubt_load_interval_b=1503971694981; ubta=3154866423.3241223259.1503971686808.1503971686808.1503971695039.2; ubtc=3154866423.3241223259.1503971695041.0EF45810F9672DC3BD68868B080BCCEE; ubtd=2; __xsptplus696=696.1.1503971687.1503971695.2%234%7C%7C%7C%7C%7C%23%23fcZh1fCVH7j7doKzh4kC96wk_XE7Y965%23; select_city=500000; _ga=GA1.2.331020171.1503638699; _gid=GA1.2.2040440312.1503909104; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1503638699; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1503984016; _gat=1; _gat_past=1; _gat_new=1; _gat_global=1; _gat_new_global=1; CNZZDATA1254525948=145009446-1503633660-%7C1503984153; CNZZDATA1253491255=851767322-1503638199-%7C1503981640; lianjia_ssid=343c0faf-c443-4673-b900-5c05298bd28a'
    #cookie='lj-ss=5bd2bc45dbdf0644d704777dc2075366; lianjia_uuid=c6a7836e-cf96-45ae-96e5-6fdb2def9fb7; UM_distinctid=15e17d9bbf960c-08e33a5d4e4891-4d015463-1fa400-15e17d9bbfa300; gr_user_id=4571568e-96d5-467c-ad95-9dd1f55471e1; ubt_load_interval_b=1503971694981; ubta=3154866423.3241223259.1503971686808.1503971686808.1503971695039.2; ubtc=3154866423.3241223259.1503971695041.0EF45810F9672DC3BD68868B080BCCEE; ubtd=2; __xsptplus696=696.1.1503971687.1503971695.2%234%7C%7C%7C%7C%7C%23%23fcZh1fCVH7j7doKzh4kC96wk_XE7Y965%23; select_city=441900; select_nation=1; _ga=GA1.2.331020171.1503638699; _gid=GA1.2.2040440312.1503909104; _gat=1; _gat_past=1; _gat_new=1; _gat_global=1; _gat_new_global=1; CNZZDATA1254525948=145009446-1503633660-%7C1503995449; CNZZDATA1253491255=851767322-1503638199-%7C1503992440; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1503638699; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1503997546; lianjia_ssid=bc9efc9f-e684-48a9-ba85-00445efd9b8e'
    #cookie='lj-ss=5bd2bc45dbdf0644d704777dc2075366; lianjia_uuid=c6a7836e-cf96-45ae-96e5-6fdb2def9fb7; UM_distinctid=15e17d9bbf960c-08e33a5d4e4891-4d015463-1fa400-15e17d9bbfa300; gr_user_id=4571568e-96d5-467c-ad95-9dd1f55471e1; select_nation=1; ubtreadd_b=116.24.65.18, 116.211.165.20; __xsptplusUT_696=1; _gat=1; _gat_su=1; ubt_load_interval_b=1504010643534; ubt_load_interval_c=1504010643534; ubtd=12; __xsptplus696=696.3.1504009165.1504010643.8%234%7C%7C%7C%7C%7C%23%23-z3bQR1R9MlwhM552JVj8NxMi25X8E56%23; gr_session_id_970bc0baee7301fa=27345ff4-a223-4916-8fd2-72741f5a2f79; ubta=4134795863.3241223259.1503971686808.1504010643547.1504010649763.12; ubtb=4134795863.3241223259.1504010649764.59CACEDE6473D431BA70CC45A3A1E9AA; ubtc=4134795863.3241223259.1504010649764.59CACEDE6473D431BA70CC45A3A1E9AA; select_city=130100; _gat_past=1; _gat_new=1; _gat_global=1; _gat_new_global=1; CNZZDATA1254525948=145009446-1503633660-%7C1504006250; CNZZDATA1253491255=851767322-1503638199-%7C1504008679; _ga=GA1.2.331020171.1503638699; _gid=GA1.2.2040440312.1503909104; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1503638699; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1504010661; lianjia_ssid=0484567a-0863-349a-eb62-4fc161820284'
    #cookie='lj-ss=5bd2bc45dbdf0644d704777dc2075366; lianjia_uuid=c6a7836e-cf96-45ae-96e5-6fdb2def9fb7; UM_distinctid=15e17d9bbf960c-08e33a5d4e4891-4d015463-1fa400-15e17d9bbfa300; gr_user_id=4571568e-96d5-467c-ad95-9dd1f55471e1; select_nation=1; ubtreadd_b=116.24.65.18, 116.211.165.20; _gat=1; _gat_su=1; ubt_load_interval_b=1504010643534; ubt_load_interval_c=1504010643534; ubtd=12; __xsptplus696=696.3.1504009165.1504010643.8%234%7C%7C%7C%7C%7C%23%23-z3bQR1R9MlwhM552JVj8NxMi25X8E56%23; gr_session_id_970bc0baee7301fa=27345ff4-a223-4916-8fd2-72741f5a2f79; ubta=4134795863.3241223259.1503971686808.1504010643547.1504010649763.12; ubtb=4134795863.3241223259.1504010649764.59CACEDE6473D431BA70CC45A3A1E9AA; ubtc=4134795863.3241223259.1504010649764.59CACEDE6473D431BA70CC45A3A1E9AA; select_city=130100; _ga=GA1.2.331020171.1503638699; _gid=GA1.2.2040440312.1503909104; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1503638699; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1504010661; _gat_past=1; _gat_new=1; _gat_global=1; _gat_new_global=1; CNZZDATA1254525948=145009446-1503633660-%7C1504006250; CNZZDATA1253491255=851767322-1503638199-%7C1504008679; lianjia_ssid=0484567a-0863-349a-eb62-4fc161820284'
    #cookie='lj-ss=5bd2bc45dbdf0644d704777dc2075366; lianjia_uuid=c6a7836e-cf96-45ae-96e5-6fdb2def9fb7; UM_distinctid=15e17d9bbf960c-08e33a5d4e4891-4d015463-1fa400-15e17d9bbfa300; gr_user_id=4571568e-96d5-467c-ad95-9dd1f55471e1; lj-api=9111950472618e41591b6800072ddacb; _jzqckmp=1; ubt_load_interval_b=1504076659297; ubta=3154866423.3241223259.1503971686808.1504062380059.1504076659413.19; ubtc=3154866423.3241223259.1504076659416.04775B09D4A0751F8665A61B54987A68; ubtd=19; __xsptplus696=696.5.1504076659.1504076659.1%234%7C%7C%7C%7C%7C%23%230CIWTVwbBidFOpEsVtab9KgnY2MeVIYe%23; sample_traffic_test=guide_card; select_nation=1; _jzqx=1.1504062784.1504090314.3.jzqsr=sz%2Efang%2Elianjia%2Ecom|jzqct=/.jzqsr=you%2Elianjia%2Ecom|jzqct=/hk; select_city=441300; _smt_uid=59a62d3f.3df2aef3; _jzqa=1.1378702697002941000.1504062784.1504083754.1504090314.4; _jzqc=1; _jzqb=1.3.10.1504090314.1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; CNZZDATA1254525948=145009446-1503633660-%7C1504087254; CNZZDATA1253491255=851767322-1503638199-%7C1504091020; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1503638699; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1504091650; _ga=GA1.2.331020171.1503638699; _gid=GA1.2.2040440312.1503909104; _gat=1; _gat_past=1; _gat_new=1; lianjia_ssid=bd082802-0db2-4698-84e5-b015007e18f3'
    #cookie='lj-ss=5bd2bc45dbdf0644d704777dc2075366; lianjia_uuid=c6a7836e-cf96-45ae-96e5-6fdb2def9fb7; UM_distinctid=15e17d9bbf960c-08e33a5d4e4891-4d015463-1fa400-15e17d9bbfa300; gr_user_id=4571568e-96d5-467c-ad95-9dd1f55471e1; lj-api=9111950472618e41591b6800072ddacb; _jzqckmp=1; ubt_load_interval_b=1504076659297; ubta=3154866423.3241223259.1503971686808.1504062380059.1504076659413.19; ubtc=3154866423.3241223259.1504076659416.04775B09D4A0751F8665A61B54987A68; ubtd=19; __xsptplus696=696.5.1504076659.1504076659.1%234%7C%7C%7C%7C%7C%23%230CIWTVwbBidFOpEsVtab9KgnY2MeVIYe%23; sample_traffic_test=guide_card; select_nation=1; _jzqx=1.1504062784.1504090314.3.jzqsr=sz%2Efang%2Elianjia%2Ecom|jzqct=/.jzqsr=you%2Elianjia%2Ecom|jzqct=/hk; select_city=441300; _smt_uid=59a62d3f.3df2aef3; _jzqa=1.1378702697002941000.1504062784.1504083754.1504090314.4; _jzqc=1; _jzqb=1.3.10.1504090314.1; CNZZDATA1254525948=145009446-1503633660-%7C1504087254; CNZZDATA1253491255=851767322-1503638199-%7C1504091020; _ga=GA1.2.331020171.1503638699; _gid=GA1.2.2040440312.1503909104; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1503638699; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1504092147; lianjia_ssid=bd082802-0db2-4698-84e5-b015007e18f3'
    #cookie='lianjia_uuid=c6a7836e-cf96-45ae-96e5-6fdb2def9fb7; UM_distinctid=15e17d9bbf960c-08e33a5d4e4891-4d015463-1fa400-15e17d9bbfa300; gr_user_id=4571568e-96d5-467c-ad95-9dd1f55471e1; all-lj=6341ae6e32895385b04aae0cf3d794b0; ubt_load_interval_b=1504076659297; ubta=3154866423.3241223259.1503971686808.1504062380059.1504076659413.19; ubtc=3154866423.3241223259.1504076659416.04775B09D4A0751F8665A61B54987A68; ubtd=19; __xsptplus696=696.5.1504076659.1504076659.1%234%7C%7C%7C%7C%7C%23%230CIWTVwbBidFOpEsVtab9KgnY2MeVIYe%23; select_nation=1; _jzqx=1.1504062784.1504090314.3.jzqsr=sz%2Efang%2Elianjia%2Ecom|jzqct=/.jzqsr=you%2Elianjia%2Ecom|jzqct=/hk; select_city=440300; _jzqckmp=1; _smt_uid=59a62d3f.3df2aef3; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1503638699; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1504159225; CNZZDATA1255849469=590735468-1504057966-null%7C1504156591; CNZZDATA1254525948=1531358740-1504060252-null%7C1504157522; CNZZDATA1255633284=355134272-1504060008-null%7C1504156303; CNZZDATA1255604082=1601457208-1504060276-null%7C1504156141; _qzja=1.218613373.1504062783783.1504083754402.1504159190536.1504159217348.1504159225576.0.0.0.33.4; _qzjb=1.1504159190535.5.0.0.0; _qzjc=1; _qzjto=5.1.0; _jzqa=1.1378702697002941000.1504062784.1504090314.1504159191.5; _jzqc=1; _jzqb=1.5.10.1504159191.1; _ga=GA1.2.331020171.1503638699; _gid=GA1.2.2040440312.1503909104; lianjia_ssid=91b42e46-ef70-501d-e228-53ee3b069ed5'
    #cookie='lianjia_uuid=c6a7836e-cf96-45ae-96e5-6fdb2def9fb7; UM_distinctid=15e17d9bbf960c-08e33a5d4e4891-4d015463-1fa400-15e17d9bbfa300; gr_user_id=4571568e-96d5-467c-ad95-9dd1f55471e1; all-lj=6341ae6e32895385b04aae0cf3d794b0; select_nation=1; _jzqx=1.1504062784.1504090314.3.jzqsr=sz%2Efang%2Elianjia%2Ecom|jzqct=/.jzqsr=you%2Elianjia%2Ecom|jzqct=/hk; _jzqckmp=1; cityCode=sh; __xsptplus696=696.6.1504164644.1504165854.10%234%7C%7C%7C%7C%7C%23%23NTqr6t6GiZMyZVzgpXGicjWjL29L2Uan%23; ubt_load_interval_b=1504165854069; ubtd=29; ubta=2299869246.3241223259.1503971686808.1504165855073.1504165862464.29; ubtc=2299869246.3241223259.1504165862465.092EC81127748E6E91BE9ED24C39F495; _ga=GA1.2.331020171.1503638699; _gid=GA1.2.2040440312.1503909104; select_city=440300; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1503638699; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1504169192; _smt_uid=59a62d3f.3df2aef3; CNZZDATA1255849469=590735468-1504057966-null%7C1504167391; CNZZDATA1254525948=1531358740-1504060252-null%7C1504168464; CNZZDATA1255633284=355134272-1504060008-null%7C1504166449; CNZZDATA1255604082=1601457208-1504060276-null%7C1504166658; _jzqa=1.1378702697002941000.1504062784.1504162491.1504164572.7; _jzqc=1; _qzja=1.218613373.1504062783783.1504164602018.1504166641481.1504169184377.1504169192487.0.0.0.44.7; _qzjb=1.1504166641480.6.0.0.0; _qzjc=1; _qzjto=16.4.0; _jzqb=1.20.10.1504164572.1; lianjia_ssid=5d09f424-3ea5-4240-ad81-024db2a8379b'
    cookie='lianjia_uuid=ca5a64ec-9cbe-4f31-8499-f06c3ea622da; UM_distinctid=15e23b039a53a7-0b6a06eff463b1-5c153d17-1fa400-15e23b039a68d1; gr_user_id=9895cc06-d162-4985-b42c-0cc98cdee98f; _smt_uid=59a36a39.a7e32ae; _jzqa=1.206544328628398600.1503881786.1503881786.1503881786.1; lj-ss=1e5c8b6bb356c2aabadd162c97341948; ubt_load_interval_b=1504537420276; ubtd=4; __xsptplus696=696.5.1504537420.1504537420.1%234%7C%7C%7C%7C%7C%23%23Dyu9Xh4KKNw0aqvAFjtibtSfVngPI3dg%23; ubta=3154866423.1593962235.1503840667336.1504537420288.1504537421470.26; ubtc=3154866423.1593962235.1504537421471.54A8769FA2903B4254B688736A67011F; select_nation=1; _gat=1; _gat_past=1; _gat_new=1; _gat_global=1; _gat_new_global=1; select_city=440300; _ga=GA1.2.885541457.1503837305; _gid=GA1.2.893652375.1504537910; CNZZDATA1254525948=1758800946-1503835682-%7C1504541662; CNZZDATA1253491255=597282999-1503832971-%7C1504541193; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1503881786,1504101487,1504454486,1504537910; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1504542040; lianjia_ssid=c76950fe-ad1d-43b6-9dbd-825dc40fc561'
    trans = transCookie(cookie)
    print trans.stringToDict()