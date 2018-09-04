# coding: utf-8
import collections
from spider.header_toolkit import urlAdd

d = urlAdd('urlparse')
arg_dict = {'ac': 'wifi',
            'app_name': 'news_article',
            '_rticket': '1506007085978',
            'ssmix': 'a',
            'item_id': '6463767286606987789',
            'from_category': '__all__',
            'device_type': 'SM801',
            'aggr_type': '1',
            'os_api': '22',
            'uuid': '990006203070023',
            'openudid': '4dd00e258bbe295f',
            'version_code': '636',
            'os_version': '5.1.1',
            'update_version_code': '6368',
            'channel': 'smartisan',
            'device_platform': 'android',
            'ab_version': '169863%2C177250%2C179334%2C173967%2C172663%2C172659%2C171194%2C176916%2C170349%2C178991%2C176179%2C177070%2C169447%2C178210%2C179194%2C168463%2C179654%2C174398%2C178732%2C178921%2C169300%2C178930%2C177166%2C179769%2C152026%2C176593%2C178581%2C176695%2C177786%2C170713%2C179768%2C179373%2C176739%2C179006%2C179751%2C156262%2C145585%2C179382%2C174429%2C177258%2C179636%2C177042%2C162572%2C176599%2C176609%2C179625%2C175163%2C169176%2C175634%2C176616%2C170988%2C178989%2C176597%2C176652%2C177702%2C176615',
            'iid': '15189530186',
            'device_brand': 'SMARTISAN',
            'manifest_version_code': '636',
            'ab_client': 'a1%2Cc4%2Ce1%2Cf2%2Cg2%2Cf7',
            'abflag': '3',
            'version_name': '6.3.6',
            'ab_feature': '102749%2C94563',
            'device_id': '38220008232',
            'language': 'zh',
            'plugin': '2431',
            'longitude': '113.902542',
            'article_page': '1',
            'flags': '64',
            'context': '1',
            'aid': '13',
            'group_id': '6463767286606987789',
            'resolution': '1080*1920',
            'dpi': '480'}

args = collections.OrderedDict([('group_id', '6463767286606987789'),
                                ('item_id', '6463767286606987789'),
                                ('aggr_type', '1'),
                                ('context', '1'),
                                ('flags', '64'), ('from_category', '__all__'),
                                ('article_page', '1'), ('iid', '15189530186'),
                                ('ac', 'wifi'), ('aid', '13'), ('app_name', 'news_article'),
                                ('version_code', '636'),
                                ('version_name', '6.3.6'),
                                ('device_platform', 'android'),
                                ('ab_client', 'a1%2Cc4%2Ce1%2Cf2%2Cg2%2Cf7'),
                                ('ab_feature', '102749%2C94563'),
                                ('abflag', '3'), ('ssmix', 'a'),
                                ('language', 'zh'),
                                ('manifest_version_code', '636'),
                                ('update_version_code', '6368'),
                                ('plugin', '2431')])

args_another = collections.OrderedDict(
    [('count', '20'), ('min_behot_time', '1506181105'), ('last_refresh_sub_entrance_interval', '1506217271'),
     ('loc_mode', '0'),
     ('tt_from', 'enter_auto'), ('lac', '42356'), ('cid', '177019578'),
     ('cp', '549bcb7b02d37q1'), ('plugin_enable', '3'), ('st_time', '9'), ('iid', '15189530186'),
     ('device_id', '38220008232'), ('ac', 'wifi'), ('aid', '13'),
     ('ab_client', 'a1%2Cc4%2Ce1%2Cf2%2Cg2%2Cf7'), ('ab_feature', '102749%2C94563'), ('abflag', '3'), ('ssmix', 'a'),
     ('language', 'zh'), ('os_api', '22'),
     ('os_version', '5.1.1'),
     ('manifest_version_code', '636'), ('update_version_code', '6368'),
     ('plugin', '2431')])

args_4 = collections.OrderedDict([('refer', '1'), ('count', '20'),
                                  ('last_refresh_sub_entrance_interval', '1506220325'), ('loc_mode', '0'),
                                  ('loc_time', '1506071873'),
                                  ('tt_from', 'pre_load_more'),
                                  ('lac', '9365'), ('cid', '3672'), ('cp', '5493c07313925q1'), ('plugin_enable', '3'),
                                  ('st_time', '333'), ('iid', '15189530186'), ('device_id', '38220008232'),
                                  ('ac', 'wifi'), ('aid', '13'), ('app_name', 'news_article'),
                                  ('version_code', '636'), ('version_name', '6.3.6'), ('device_platform', 'android'), (
                                      'ab_version',
                                      '179886%2C169863%2C177250%2C179334%2C173967%2C172663%2C172659%2C171194%2C170349%2C178991%2C176179%2C177070%2C169447%2C178210%2C179194%2C168463%2C174398%2C178732%2C178921%2C169300%2C178930%2C180698%2C177166%2C152026%2C176593%2C180172%2C179891%2C178581%2C177786%2C170713%2C179373%2C176739%2C179006%2C156262%2C145585%2C180654%2C179382%2C174429%2C177258%2C180186%2C177042%2C162572%2C176599%2C176609%2C179625%2C175163%2C169176%2C175634%2C176616%2C170988%2C178989%2C176597%2C176652%2C177702%2C176615'),
                                  ('ab_client', 'a1%2Cc4%2Ce1%2Cf2%2Cg2%2Cf7'), ('ab_feature', '102749%2C94563'),
                                  ('abflag', '3'), ('ssmix', 'a'), ('device_type', 'Galaxy'),
                                  ('language', 'zh'),
                                  ('os_version', '5.1.1'), ('uuid', '990006203070023'),
                                  ('openudid', '4dd00e258bbe295f'), ('manifest_version_code', '636'),
                                  ('update_version_code', '6368'),
                                  ('plugin', '2431')])

args_5 = collections.OrderedDict([('refer', '1'), ('count', '20'), ('max_behot_time', '1506210972'),
                                  ('last_refresh_sub_entrance_interval', '1506220325'), ('loc_mode', '0'),

                                  ('city', '%E6%B7%B1%E5%9C%B3%E5%B8%82'), ('tt_from', 'pre_load_more'),
                                  ('lac', '9365'), ('cid', '3672'), ('cp', '5493c07313925q1'), ('plugin_enable', '3'),
                                  ('st_time', '333'), ('iid', '15189530186'), ('device_id', '38220008232'),
                                  ('ac', 'wifi'), ('channel', 'smartisan'), ('aid', '13'), ('app_name', 'news_article'),
                                  ('version_code', '636'), ('version_name', '6.3.6'), ('device_platform', 'android'), (
                                  'ab_version',
                                  '179886%2C169863%2C177250%2C179334%2C173967%2C172663%2C172659%2C171194%2C170349%2C178991%2C176179%2C177070%2C169447%2C178210%2C179194%2C168463%2C174398%2C178732%2C178921%2C169300%2C178930%2C180698%2C177166%2C152026%2C176593%2C180172%2C179891%2C178581%2C177786%2C170713%2C179373%2C176739%2C179006%2C156262%2C145585%2C180654%2C179382%2C174429%2C177258%2C180186%2C177042%2C162572%2C176599%2C176609%2C179625%2C175163%2C169176%2C175634%2C176616%2C170988%2C178989%2C176597%2C176652%2C177702%2C176615'),
                                  ('ab_client', 'a1%2Cc4%2Ce1%2Cf2%2Cg2%2Cf7'), ('ab_feature', '102749%2C94563'),
                                  ('abflag', '3'), ('ssmix', 'a'), ('device_type', 'SM801'),
                                  ('device_brand', 'SMARTISAN'), ('language', 'zh'), ('os_api', '22'),
                                  ('os_version', '5.1.1'), ('uuid', '990006203070023'),
                                  ('openudid', '4dd00e258bbe295f'), ('manifest_version_code', '636'),
                                  ('resolution', '1080*1920'), ('dpi', '480'), ('update_version_code', '6368'),
                                  ('_rticket', '1506220325881'), ('plugin', '2431')])

base = 'http://lf.snssdk.com/2/article/information/v23/?'
base2 = 'http://lf.snssdk.com/api/news/feed/v66/?concern_id=6286225228934679042&'
base3 = 'http://lg.snssdk.com/api/news/feed/v66/?concern_id=6286225228934679042&'
arg_list = []
print(d)
for k, v in args_5.items():
    arg = k + '=' + v
    arg_list.append(arg)
post_url = '&'.join(arg_list)
url = base3 + post_url
print(url)
