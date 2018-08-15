# coding: utf-8
import json
import urllib

import requests
# coding: utf-8
import json
import random
import urllib
from urllib import quote
import MySQLdb
import datetime
import requests
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import redis
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, Text, INT
#from mayidaili import useproxy

engine = create_engine('mysql+pymysql://root:@localhost:3306/test1?charset=utf8')
DBSession = sessionmaker(bind=engine)
Base = declarative_base()
session = DBSession()


class Advertiser(Base):
    __tablename__ = 'tb_advertiser1'

    id = Column(Integer, primary_key=True)
    advertiser_name = Column(String(80))
    title = Column(String(300))
    ad_url = Column(Text)
    pic_url = Column(Text)
    type = Column(String(50))
    source = Column(String(80))
    crawl_time = Column(DateTime, default=datetime.datetime.now())
    exposure = Column(INT, default=1)
    deeplink = Column(String(300))
    desc = Column(Text)

class AdvertiserOrg(Base):
    __tablename__ = 'tb_advertiser'

    id = Column(Integer, primary_key=True)
    advertiser_name = Column(String(80))
    title = Column(String(300))
    ad_url = Column(Text)
    pic_url = Column(Text)
    type = Column(String(50))
    source = Column(String(80))
    crawl_time = Column(DateTime, default=datetime.datetime.now())
    exposure = Column(INT, default=1)

Base.metadata.create_all(engine)
headers = {'Accept-Encoding': 'gzip', 'Charset': 'UTF-8', 'Connection': 'Keep-Alive', 'Accept': 'application/json',
           'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM801 Build/LMY47V)', 'Host': 'news.l.qq.com',
           'Content-Type': 'application/json'}


def storedata():
    advertiser = session.query(Advertiser).all()
    print(len(advertiser))
    for i in advertiser:
        #print(i.advertiser_name)

        obj = AdvertiserOrg(
            advertiser_name=i.advertiser_name,
            title=i.title,
            ad_url=i.ad_url,
            pic_url=i.pic_url,
            type=i.type,
            source=i.source,
            #deeplink=itedeeplink']
            crawl_time=i.crawl_time,
            exposure=i.exposure
        )
        session.add(obj)


        try:
            session.commit()
        except Exception as e:
            print(e)
            session.rollback()


def get_advertiser():
    r_session=requests.Session()
    source = u'腾讯新闻'
    url = 'http://news.l.qq.com/app'
    data_option1={"adtype":1,"pf":"aphone","ifa":"2b8bbc0c-03c1-41cb-8ed1-f42305977349","app_channel":"3772","ext":{"mob":{"mobstr":"AdiIlDlcnKXLQu1Gx+HOa9fZY4dnXP8U1t2\/DxOZD2HmbcVCQtuntpciIn\/4qHXgFB+gz9SlS4yWsWk9DQgKPqRHl8h4+Nw+7Edne3huSN1DwSkptLOGfOe0f+tcC8jHP4QP6jQ0afF3y5QuRRWLySHcBMyxthBVqDD8opccNjPKmadCrlceaWUZyV3mJNTNpBgueP7AdxCGuUgEG2NRG7sWML3zwb1kuFFboY5yq6JY93HPwR2kDCCMnYfZ9vSTHGphriWm0q7FI3cDlmPxUG73RysfPRVyDJEmhGGPGxEEjRswxD6fbEBZeK6kNI3GR8zGtDjaygTUowesyU1oqF4+vstcV4K67WJZ59qiE08xf++TWWJd+wwlJFdgsJ\/sCKyAOv+RRsUvISeF+r8irRK7ZHMKKR67o+oN0eKi6FJL93oYbvNsOuY\/sCw4U20HXsVS1mIod+mj0z3S24UKVPFS9yfV5Clj1eUrBA3RBG2ifDlvzaPqXOOZWE\/M5q2CG8xoHCjZPzs1uk48bsYvk08vYA58uca8Ex4eY99YjIjLTOepwfIEqWme0e8Y+0tY5BbtXoRGChLRrE8TgiP8EmivbVQcM1yh6mRqJJgj6a7T7eDvUhrnBAEnwCgJWneYxKu+XFUbWiQBSKbHtAQh6fNp\/noXw9610pU5D61r3lkrA8hspUStmB3AF2Zq9otYzE\/vZkpr8iU\/8\/mjqhpNLJp82XJMO4hotQFK\/itcBXTx9xh9P4Whrv0Y79Pk4Zt1U0J1xSm+gWFBC3OLACirM1GypHFgT2qZDG+MGAW1H2Pi683\/+QIgy1SHraLM2lAR27S7rNvruo+UKLaWn13WoRYDQrKOfAr+PgXwggH4pwfEe\/wL9kXBwx1rm9qZnyQusUIl3wQVO\/MmwefaZA5s+J0fI\/5b7loz+aeMK0+VJaSm0T7rL+VrQ1SOPaVdCtInZ2OJOHrIu6KvOhkckr+n4ETDkbnjDdpPZGtrUf0frBh8CGVFipFG0JMu\/qXU61yu+E1hGrVufvPSu++p+1FB3N71OBjDBpU3sUU9yTwTX3g8kHd\/+wZkM8wZ4GZCVuUvMRYcpB\/CeWjF5GHMK+2P8WiHVrOCybLjulb1Udo3kVrp\/Vrnq2h+wtYCNFcMfOrTneHS\/zf78XPntvLYGkakfxU="}},"appversion":"170920","chid":2,"slot":[{"loid":"1","channel":"news_news_sports","index":"1,2,3,4,5,6,7","rot":"3606017,3541195,3602207,3616217,3612537,3602029,3564939","cur":34}],"uin":"445636075"}
    data_option2={"adtype":1,"pf":"aphone","ifa":"2b8bbc0c-03c1-41cb-8ed1-f42305977349","app_channel":"3772","ext":{"mob":{"mobstr":"AdiIlDlcnKXLQu1Gx+HOa9fZY4dnXP8U1t2\/DxOZD2HmbcVCQtuntpciIn\/4qHXgFB+gz9SlS4yWsWk9DQgKPqRHl8h4+Nw+7Edne3huSN1DwSkptLOGfOe0f+tcC8jHP4QP6jQ0afF3y5QuRRWLySHcBMyxthBVqDD8opccNjPKmadCrlceaWUZyV3mJNTNpBgueP7AdxCGuUgEG2NRG7sWML3zwb1kuFFboY5yq6JY93HPwR2kDCCMnYfZ9vSTHA6kzJXPbNBaa8ia3Vbo+UU2dfU53AUg71hWhgYxzmdNbf8rNe4umXVs4m6VwTpKBcg\/oMCuZhd+9xKN016M2AlJCQ1t2\/xtyx5eGRGa0PgVAwpwjk2yhUNpae64281z7xbdUjDkyZBRKJMFavjYge0WSwcfhbbPejJOXmFU2xuNbwRYBCuaQKq51uzoB5T\/jZBzhobWBvkNoXb90JsSXZqC9C68TBWWL4KDG5sR4bYTmsFAOG0XEZX4A5ygiRAZLdBTC9NNbiNVJfGXaffxTNT2V2unWJhhS1XMZ467fTX1GRvH8kp0kivB\/pKdquC4qNWQjIESU2Cq7VTZ3vF4OcKSMKOjWVj0s3F4b2J04yUep+z2xOk762BV\/XfwFbF7NX\/Mu1qy3Xr3JDVQbdeO5IPIoTvxD5xUdy2W6FmFRJKRP+RNbX90lF8jfM1GbUgYb2yxwnDoBIokkDcl0sfcGLm0foOcLkScwFUXjmb\/dUNNejiSGHrVSedgxTYeCLUYvnZ+i9zF56XQenTVnyeHhW0sBLeu\/tgWfv\/vFJXYq6XCOAm1KiIxavnB8XZOgZuVWe3MH+bzGbKAS68V1tlv9na20uhK\/eDK\/RyLX319RXUa8hPyaKl93hcBmtZWndERWQDKUq+dJ3ZCkUBmkY\/uuoE\/Rl8z8XnL+rCVHDAP\/XNt5kDuA+5EF+ogEAQtZdF7vHKUGCFqgDsaOjDGVw0i3lelnWEWxtJ6XjKy1TVj3w4UbzAGhGyF0PYVIKnWJfvRvZP6bynyE940eGzNtm266z6hWRxMxHXeE9lSlN+hXtIPfouYycWCIYAAjfsZhsw8UsLzinZaADsBRwR3dq2gLoIZA3JoGarYBIB8v44LH\/C2QH99Pqr6qUopwMZhr7PAApcDHKTJRzScCzzoXA0iGhg="}},"appversion":"170920","chid":2,"slot":[{"loid":"1","channel":"news_news_ent","index":"1,2,3,4,5,6,7,8,9,10,11","rot":"3602207,3616217,3602029,3543531,3612825,3612537,3564939,3606017,3541195,3607261,3519647","cur":80}],"uin":"445636075"}
    data_option3={"adtype":1,"pf":"aphone","ifa":"2b8bbc0c-03c1-41cb-8ed1-f42305977349","app_channel":"3772","ext":{"mob":{"mobstr":"AdiIlDlcnKXLQu1Gx+HOa9fZY4dnXP8U1t2\/DxOZD2HmbcVCQtuntpciIn\/4qHXgFB+gz9SlS4yWsWk9DQgKPqRHl8h4+Nw+7Edne3huSN1DwSkptLOGfOe0f+tcC8jHP4QP6jQ0afF3y5QuRRWLySHcBMyxthBVqDD8opccNjPKmadCrlceaWUZyV3mJNTNpBgueP7AdxCGuUgEG2NRG7sWML3zwb1kuFFboY5yq6JY93HPwR2kDCCMnYfZ9vSTHI33qirMXz7JHbRJ8Q6Silw7o09ZZZ5\/I9W9RGPXgpG7NB1+oh1PiCGi8k6naxH+xJHAW\/fW47\/eCk44TVGURbDjcOTDH9Nd8XeJRGL8+fAOclaSdcdmMf2I\/EStAZOzo5T08RpGVCkwvWAafhWvGgwiv3AsRiKuf62+dM\/BOmNcRrUJwJbrFRehl4ZHV+y4nv+9YLXoPwHwhm1CBfQfCw6hRU5vUrYqZfTli+oLmOOf0KRZ+WEJ7vP+3buaumoGm9CEIxs05YkzvvxcUV4qrBPbMiPUziBFfknubfz38Dls+XOQQyHrFL\/LMWU\/0Q8gYn+FY62EzDnvEMRcVaFAOuuWGHgIRZixh4JHbr1dt5Q2c7\/UBJ8bgZiImykM4yQr4bM9iUtqDj6NkTHpIkUIFW4rAYpiHCoVyq8IRkEn\/l2EQsxsa\/f4\/ocyF5CblDgK37rHj30UR6n7p5lvw\/nVPGdgwLfX1+qfqB+KG4HVWlZyDMwZfaAtHlB1rLZ87E44MHI3XNVEerwgH\/zXlDiySMqIm7eooL3n3VvBAhgItWb6SLAJtjpx\/elTQwcJChtrrgVV9b0JHPImua7RXLlrdVxtlG7y3ND1VTztw50cunIfISzQ2lpx+N49MpmXU8QeG604qCLL4inO5YjJ+dcRCfm00Mhyp+taXy4I9CiL0iBTUVSOSs96lFSM0Go8OYcaeVC+JdTEnT6z+1GD8h6xyxiv4aLhIkqU2eki0m44To5oj7ZbZFFYHy6A2qXD8JZcQ+YzA9JHuEzyPc0ct8kmrDno9ksddM\/atlL9F+jNSGc\/cyGZQIsFDpgRjV2g\/cd5Z5LRCnAG4+vYgUiTAMof2JDNVSskt9GRZP2KozHvOR4FWZVzmfZShf+S5GRiqAuXlTlu6lG0ASIP1\/GHCa\/rZGQ="}},"appversion":"170920","chid":2,"slot":[{"loid":"1","channel":"news_news_ent","index":"1,2,3,4,5,6,7","rot":"3602207,3616217,3602029,3543531,3612825,3612537,3564939","cur":36}],"uin":"445636075"}
    data_option4={"adtype":5,"pf":"aphone","ifa":"2b8bbc0c-03c1-41cb-8ed1-f42305977349","app_channel":"3772","ext":{"mob":{"mobstr":"AdiIlDlcnKXLQu1Gx+HOa9fZY4dnXP8U1t2\/DxOZD2HmbcVCQtuntpciIn\/4qHXgFB+gz9SlS4yWsWk9DQgKPqRHl8h4+Nw+7Edne3huSN1DwSkptLOGfOe0f+tcC8jHP4QP6jQ0afF3y5QuRRWLySHcBMyxthBVqDD8opccNjPKmadCrlceaWUZyV3mJNTNpBgueP7AdxCGuUgEG2NRG7sWML3zwb1kuFFboY5yq6JY93HPwR2kDCAOZa2YuNpB5MSLgaZ9L\/kxNj09MBius9btM1PkZkgGIpOj6ZuSGpsn\/8\/7Q4byBioqBPonjQQC2wPJAJ0E7kd5PCyBAX2idSLxIFZi\/1Z4G+QxRs1\/m1NQI070WkL8kt3MDnLjt87CqN3UdClE1lhDRUexsALjg7lw6puCq88YokIjB2I4zrkpILDzEW0etdQsk1o7N5YjMuhUF+HZ54Xyz2cCewQAznxyEUX5jysyhmnySyugrKpkj+zIRWY352KGph\/LN\/jXdawfKaq0YkrZm6ZyERcjFZHrQS6gHhDJ2ERV6wcuLzF4MjuhiuwUoEK5U3TedONafQ9Ugsvq27u2\/mNl+dyXl4f5HLfVsUj5nqNGD6hyJkLLoCZhVCzAycacF1PchsKL03nPxnHoM0FoNkEdiqbjm58RvrGzmSrdV7ahmyFbMy+5cHKatpRbDcSEcfJ9p+WjADY1jJDHdCy3atsmTixhC\/BmJddjhdmOkAhJGhDhkQxNf+e1IheQ+lWgGQMDOglNYRbiKxf8Y35C\/VRBhYvlAfBvqweuXblcfWN8QnJ+uvWxNB24VYt3A4Z9NHUTIADVLUO6barnuDExVt3qywDMOiiyydLz9yhz5hJLo2hVKOiSGNy1Lsxx3lh3PeTVM8avQuaoPLlZNDu454j+3bDKiNqS0PwIE0E2MMGUyXG+7hWz3OHxIGSgQLnb5ieBiPf6yG3NEf\/OiCOLqjJVn15VwJKKPmNQ5Z9KE25HPHnUavPY\/e+2VjxZnHzY0NzKktZmMXvJkUkFWfpH+g+fIxQU4b1oV4h66GKbJf\/Vpas7kMFXsAsgtNAfeRU4wPP1XC+yH3kqh3dBDokJuBPSvtG5QZz+QzrgmQsDd48GSFsGmCJsb9OwrZ9BY1JMNjHs5bCpAqgvPjphDJxXQf60842FO64="}},"appversion":"170920","chid":2,"slot":[{"loid":"1,4","channel":"news_news_top,news_recommend_main,news_news_sz","rot":"3606017,3597395,3495423,3543531,3601429,3609813,3602029;3606017,3495423,1805489736,1805628411,1805798507,1805726199,1805689415;3495423,3604057,3609813,3543531,1100031128,3602029,1805751243"}],"uin":"445636075"}
    data_option5={"adtype":5,"pf":"aphone","ifa":"2b8bbc0c-03c1-41cb-8ed1-f42305977349","app_channel":"3772","ext":{"mob":{"mobstr":"AdiIlDlcnKXLQu1Gx+HOa9fZY4dnXP8U1t2\/DxOZD2HmbcVCQtuntpciIn\/4qHXgFB+gz9SlS4yWsWk9DQgKPqRHl8h4+Nw+7Edne3huSN1DwSkptLOGfOe0f+tcC8jHP4QP6jQ0afF3y5QuRRWLySHcBMyxthBVqDD8opccNjPKmadCrlceaWUZyV3mJNTNpBgueP7AdxCGuUgEG2NRG7sWML3zwb1kuFFboY5yq6JY93HPwR2kDCAOZa2YuNpB5Op1PxVsex7Xtmg8rvXUdCQvKZROTZRNXJFLGEHmsOX8Hy\/385oC\/ITM+sxfByxOD5k6PeTZdPheFiBmP+LM3Ae7UXGBYHvxCgNRWltvGfA48o74vvmVi0viZLuWk1+1iVdYJW4qMq7NcWILVsHtcd12oUDsvgtI1vs5Iei\/THln1MEtfNRmUX+ALbsY9WPyzqxnuSY6O4xczdEzL2Xzms7rltK7OqQbtQYfCtelwOv\/PLxmJ3aNrycg9JhIohYLt+7VR75i6HwB7ur1cECqKcpaQUeF9zkk0ExFETe++jqGz8LM1fTt8pNCPSqFQI2wj1Ht\/sIV\/sgxpP4zpjKTusuazydx5357PYB1GvjX8WUXOAQi88BYvO4NmGnuefYC9sGV1EXxN5fvQmkw\/hOZyV9LT9+Xcm9cPX+bWbcXA3wDlOVOYhA+34idoDMSp3ClxyeV1egwPurWkK87QKvhT45yOQerujwyD7VaIC5mh0odsN3WRCttSVKURJfRQVdCmNhujjQ8xGrLXmps6j6JvsIAMsf353Vq+DzvBFtL\/d+KwfeajtXUp5yP60H3aPI1ZZGBnG9mTTXE2iw5QrUB+3yRf7gyJLg9jeT4yrYx3Dy6z2O47ouMrHryKCiiSPjaCKqlRpyGo6v+azUa0HY6d\/AjACO7Vns+nmGEt8uHnNKc8YoGtKhc3ZAda7JPuK8QYpK7nyeb9ozZfIN7+yhdtNbQKrW7cvb5\/VysDp63q7wp2iR3Cem+3tdhN+VQZ17ZpU2akpEgLLbPiQ+ulqWzokrctOFG81vV7R2BjFbVnCAWcKGzlbEZSSmwUndXKFxgE0SYzRaEU+vyYBc4i8K5Jd6qf63QPtSMDOfJAx8zd\/VHqy7yt+PxU06oEsHaBhDMshrV4IP4roUCiWRw\/8QeW58="}},"appversion":"170920","chid":2,"slot":[{"loid":"1,4","channel":"news_news_mil,news_news_astro,news_news_msh","rot":"3606017,3495423,3601509,3543531,3606831,1805798507,1804441609;3606017,3495423,3601429,3543531,3598293,3598407,3606831;3541195,3606017,3495423,3543531,3605159,3601429,3598407"}],"uin":"445636075"}
    data_option6={"adtype":1,"pf":"aphone","ifa":"2b8bbc0c-03c1-41cb-8ed1-f42305977349","app_channel":"3772","ext":{"mob":{"mobstr":"AdiIlDlcnKXLQu1Gx+HOa9fZY4dnXP8U1t2\/DxOZD2HmbcVCQtuntpciIn\/4qHXgFB+gz9SlS4yWsWk9DQgKPqRHl8h4+Nw+7Edne3huSN1DwSkptLOGfOe0f+tcC8jHP4QP6jQ0afF3y5QuRRWLySHcBMyxthBVqDD8opccNjPKmadCrlceaWUZyV3mJNTNpBgueP7AdxCGuUgEG2NRG7sWML3zwb1kuFFboY5yq6JY93HPwR2kDCAOZa2YuNpB5MSLgaZ9L\/kxNj09MBius9btM1PkZkgGIpOj6ZuSGpsn\/8\/7Q4byBioqBPonjQQC2wPJAJ0E7kd5PCyBAX2idSLxIFZi\/1Z4G+QxRs1\/m1NQI070WkL8kt3MDnLjt87CqN3UdClE1lhDRUexsALjg7lw6puCq88YokIjB2I4zrkpILDzEW0etdQsk1o7N5YjMuhUF+HZ54Xyz2cCewQAznxyEUX5jysyhmnySyugrKpkj+zIRWY352KGph\/LN\/jXdawfKaq0YkrZm6ZyERcjFZHrQS6gHhDJ2ERV6wcuLzF4MjuhiuwUoEK5U3TedONafQ9Ugsvq27u2\/mNl+dyXl4f5HLfVsUj5nqNGD6hyJkLLoCZhVCzAycacF1PchsKL03nPxnHoM0FoNkEdiqbjm58RvrGzmSrdV7ahmyFbMy+5cHKatpRbDcSEcfJ9p+WjADY1jJDHdCy3atsmTixhC\/BmJddjhdmOkAhJGhDhkQxNf+e1IheQ+lWgGQMDOglNYRbiKxf8Y35C\/VRBhYvlAfBvqweuXblcfWN8QnJ+uvWxNB24VYt3A4Z9NHUTIADVLUO6barnuDExVt3qywDMOiiyydLz9yhz5hJLo2hVKOiSGNy1Lsxx3lh3PeTVM8avQuaoPLlZNDu454j+3bDKiNqS0PwIE0E2MMGUyXG+7hWzTFwClUIM1UJWLAwNPbJU7cn42sNgxF7HXPQzcKU8sU5HFgvywcWncagxlsaKTJkj3LYugt5cfVW4wnGIGdXPIU1ZCtJvIIzhjVowX76ty2y4ewqFO9HgiYGWo8ZgoowjYXPZ3Q0ZObvdwBCLWnBM9gKfgipfWTLRI+mI8RCjfroH9As2X0aRG0HaUmjdVsxWIQZAsv6z9zco4FjMzxnntygVJAWuBky72UQltEUKNf4="}},"appversion":"170920","chid":2,"slot":[{"loid":"1,4","channel":"news_news_top,news_video_top","rot":"3610157,3541195,3596849,3602207,3605159,3616217,1805792870;3495423,3601429,3598407,1805812735,1805733385,1805244749"}],"uin":"445636075"}
    data = {"adtype": 1, "pf": "aphone", "ifa": "2b8bbc0c-03c1-41cb-8ed1-f42305977349", "app_channel": "3772", "ext": {
        "mob": {
            "mobstr": "AdiIlDlcnKXLQu1Gx+HOa9fZY4dnXP8U1t2\/DxOZD2HmbcVCQtuntpciIn\/4qHXgFB+gz9SlS4yWsWk9DQgKPqRHl8h4+Nw+7Edne3huSN1DwSkptLOGfOe0f+tcC8jHP4QP6jQ0afF3y5QuRRWLySHcBMyxthBVqDD8opccNjPKmadCrlceaWUZyV3mJNTNpBgueP7AdxCGuUgEG2NRG7sWML3zwb1kuFFboY5yq6JY93HPwR2kDCAOOv5sw8soCvNq7VxhrXux+dzqePDHiDy9FM2KMShtDG2BR1Q713kTdFlzNdi94ttXV384GizaKfENslDXcrjKui2uiaFtCB3\/WvcqJl9uQIO2V5zc+372Ul1VloY\/Mc6aV1q+4KMS7daWuPHUwZTrQEVMGdafPqN9Y2z4g4gjgAKABsia1OMoY1eDYNgC3Wl8CUohURa1nUIwAw6+RaMSUsubFMmur7LODoG98ShDgQVm+XI0ACKpAEZjmQV8DOwEOSD1x5mBwqCoz9CehRjy0dzFs6VxskkuaRDoKn0P4dGRpbUrDLRAblklEIMKK3lQukpXZzLD7aiMVNJxsR9fr9OqmiB0Lq40AwNvdgQ43ObgVuT4rTMGmVVP0lsFmLfo3XgRgpW7IdkZPHUQSSBWjQpYM\/jtHR3gJG2p\/2pXrtHOg6w\/i0v2bQD3jDX1982Nhu8pHbVk\/iBTh5oY+DPt3jjj6bRSdj7HJQ99\/I7hMc3xiibPG9RyS5Cx5alPEsx4I5xVhnPxxRzXMzR1J8iJKRjvFpCHzaSIPXv8lR+xnzgCt3B48ObRPpK\/arYYRpHmdM\/PjF6P9C9kOVGzhzYKasbS+BL4fWrnPVTyprkNAMdLpPSKnmfD6OlsnL3ilUtoBj\/jsV5z9NElYiqbU3\/qMohBSixFX3FzwyQi1pKqajNHG+vKeVUcT1VTR0lJxWeDjKIN3TKVaMnd+BBM0VHs4IMGsX6x367I3pKbbMQPipq3I4jNckm5WXV1fWQH\/tL+jCf+X4aXVpdlOfnlODqQVT4oSwEmimRAjTzqLxHuRyuL2fpNh3vagCg1kSXh5BtI5bSoQRjdU9MT5iUCEuEN9ORJ9ynDDgJemPcegfVJ7Oufb6IpEwAgx0OF6gHHgCQoORvUL3\/3I1x2lb9WQOcp"}},
            "appversion": "170920", "chid": 2, "slot": [
            {"loid": "1", "channel": "news_news_top", "index": "1,2,3,4,5,6,7",
             "rot": "3606017,3535225,3601429,3543531,3602563,1805628411,1805533140", "cur": 35}]}
    data1 = {"adtype": 1, "pf": "aphone", "ifa": "2b8bbc0c-03c1-41cb-8ed1-f42305977349", "app_channel": "3772"}

    data2 = {"adtype": 1, "ifa": "2b8bbc0c-03c1-41cb-8ed1-f42305977349", "ext": {
        "mob": {
            "mobstr": "AdiIlDlcnKXLQu1Gx+HOa9fZY4dnXP8U1t2\/DxOZD2HmbcVCQtuntpciIn\/4qHXgFB+gz9SlS4yWsWk9DQgKPqRHl8h4+Nw+7Edne3huSN1DwSkptLOGfOe0f+tcC8jHP4QP6jQ0afF3y5QuRRWLySHcBMyxthBVqDD8opccNjPKmadCrlceaWUZyV3mJNTNpBgueP7AdxCGuUgEG2NRG7sWML3zwb1kuFFboY5yq6JY93HPwR2kDCAOOv5sw8soCvNq7VxhrXux+dzqePDHiDy9FM2KMShtDG2BR1Q713kTdFlzNdi94ttXV384GizaKfENslDXcrjKui2uiaFtCB3\/WvcqJl9uQIO2V5zc+372Ul1VloY\/Mc6aV1q+4KMS7daWuPHUwZTrQEVMGdafPqN9Y2z4g4gjgAKABsia1OMoY1eDYNgC3Wl8CUohURa1nUIwAw6+RaMSUsubFMmur7LODoG98ShDgQVm+XI0ACKpAEZjmQV8DOwEOSD1x5mBwqCoz9CehRjy0dzFs6VxskkuaRDoKn0P4dGRpbUrDLRAblklEIMKK3lQukpXZzLD7aiMVNJxsR9fr9OqmiB0Lq40AwNvdgQ43ObgVuT4rTMGmVVP0lsFmLfo3XgRgpW7IdkZPHUQSSBWjQpYM\/jtHR3gJG2p\/2pXrtHOg6w\/i0v2bQD3jDX1982Nhu8pHbVk\/iBTh5oY+DPt3jjj6bRSdj7HJQ99\/I7hMc3xiibPG9RyS5Cx5alPEsx4I5xVhnPxxRzXMzR1J8iJKRjvFpCHzaSIPXv8lR+xnzgCt3B48ObRPpK\/arYYRpHmdM\/PjF6P9C9kOVGzhzYKasbS+BL4fWrnPVTyprkNAMdLpPSKnmfD6OlsnL3ilUtoBj\/jsV5z9NElYiqbU3\/qMohBSixFX3FzwyQi1pKqajNHG+vKeVUcT1VTR0lJxWeDjKIN3TKVaMnd+BBM0VHs4IMGsX6x367I3pKbbMQPipq3I4jNckm5WXV1fWQH\/tL+jCf+X4aXVpdlOfnlODqQVT4oSwEmimRAjTzqLxHuRyuL2fpNh3vagCg1kSXh5BtI5bSoQRjdU9MT5iUCEuEN9ORJ9ynDDgJemPcegfVJ7Oufb6IpEwAgx0OF6gHHgCQoORvUL3\/3I1x2lb9WQOcp"}},
             "appversion": "170920", "chid": 2, "slot": [
            {"loid": "1", "channel": "news_news_top", "index": "1,2,3,4,5,6,7",
             "rot": "3606017,3535225,3601429,3543531,3602563,1805628411,1805533140", "cur": 35}]}
    data3 = {"adtype": 5, "pf": "aphone", "ifa": "2b8bbc0c-03c1-41cb-8ed1-f42305977349", "app_channel": "3772",
             "ext": {"mob": {
                 "mobstr": "AdiIlDlcnKXLQu1Gx+HOa9fZY4dnXP8U1t2\/DxOZD2HmbcVCQtuntpciIn\/4qHXgFB+gz9SlS4yWsWk9DDgKPqRHl8h5+Nw+7Edne3huSN1DwSkptLOGfOe0f+tcC8jHP4QP6jQ0afF3y5QuRRWLySHcBMyxthBVqDD8opccNjPKmadCrlceaWUZyV3mJNTNpBgueP7AdxCGuUgEG2NRG7sWML3zwb1kuFFboY5yq6JY93HPwR2kDCAOOv5sw8soCgrC36F58+yI\/1+1GMCVBkBwA\/2HGY5bNLpsJq57zERopZKsifbAHz\/rTVHjiCuR4Mt9B3Hczuq5L63r12krVHAKUllTdVQuNs9RBxlag\/ud21B+0GrV\/j7tvy8RFtMbyB+F8rcy96cnrv55eJXyJ8bpqsAzQSFlE8AX9poMsfF3SY0fBJsC8T\/EF8X9iO12CH1czI8cQMwpmaIUD0bKvubzjEKcABa0Fr2QvGuuESETcdeSnVunz777plKEjPA\/XM8GeHqFIrMUU7NJiNGzmuthLx\/XscSnFh8K4EVTuRB4mZC\/zDnogk9uQQ82Td0GDxHZEbiEvoCRAmrp1dRN3xOr3daziuH3JMpTXqtXaViYmGlrNK3zrepiISsOUgUdrWLBMX4C7jI6UNu0FH5uqTosNWcS8H7Ac7SAzPNvlAAxTeXlnyP4IqrL\/VIwMw43SpaXEwGYFp5nuS4SIe+S1wUIK5FWMF2jtbSHpmRhNF8hPTkg2ITm9SEbP569uARpuqw8ggDjXmRnzFnrsAZ1GN1QVggzD0cCORM58juRlJRqu6xsjHbcBUY1RaMNBljkTkMt5uIBb2b6mKGW6CNYD6O3LADHAaHvkEVTDZq1OCSsKgTahiryVox\/7Y4q8857KXiW3WO8gkdYNSnbVl0z0vp8Z3rTEsaYP5s3j58BprFvPSHl7Wp1XW+Fe572MWnt4HYBtqwtPzFZqdXJdwwJsEA+r\/+ZeAQTkmeZchfeGmVX49\/LzX0qV\/VKh++kFBEBdv+137nr2TmTaxF\/jyzvrlbu1CkrE+kDdqSZ+BxuUhCbRcU8Pr1w92\/w76CQ\/7UUn5NXgXpUSjHwRasnGCrND5r9JIm135Q+a5NPG+BoIBrOvIw8Cf0VzlAKP9rwNSVhi2z9umPpMs7b"}},
             "appversion": "170920", "chid": 2, "slot": [
            {"loid": "1,4", "channel": "news_news_top,news_recommend_main,news_news_ent,news_news_finance,news_news_sports,news_news_tech,news_news_mil,news_news_digi,news_news_nba",
             "rot": "35851431,35917471,36014291,35435311,3602563,3601937,3605159;3606941,3602563,3606017,3601937,3585143,3591747,3601429;3606017,3585143,3591747,3543531,3601429,3602563,3601937"}]}

    post_data=random.choice([data_option1,data_option2,data_option3,data_option4,data_option5,data_option6,data,data3,data2])
    s = json.dumps(post_data)
    # data=urllib.quote(data)

    try:
        r = r_session.post(url=url, data=s, headers=headers)
        print('statues code ', r.status_code)
        ret_data = r.json()
    except Exception as e:
        print(e)
        return
    if not ret_data.has_key('order'):
        return

    #print(json.dumps(ret_data, indent=4, sort_keys=True))
    for i in ret_data.get('order'):
        # if i.has_key('open_scheme'):
        deep_link = i.get('open_scheme', '')
        items = dict()
        title = i.get('title', '')
        advertiser_name = i.get('navTitle')
        desc = i.get('abstract', '')
        ad_url = i.get('url', '')
        pic_url = i.get('thumbnails', '')
        print('len of pic ', len(pic_url))

        if len(pic_url) == 0 and (i.has_key('resource_urlList')):
            pic_url = i.get('resource_urlList')[0].get('url', '')
        elif len(pic_url) == 0 and (i.has_key('resource_url0')):
            pic_url = i.get('resource_url0')
        elif len(pic_url) == 0:
            pic_url = ''
        print('pic url ', pic_url)
        print(advertiser_name)
        items['advertiser_name'] = advertiser_name
        items['title'] = title
        items['ad_url'] = ad_url
        items['pic_url'] = pic_url
        items['deeplink'] = deep_link
        items['desc'] = desc
        items['source'] = source
        items['type'] = 'h5'
        # items['crawl_date']=
        storedata(items)


storedata()