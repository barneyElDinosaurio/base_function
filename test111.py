# -coding=utf-8-*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from sqlalchemy import create_engine
import pymysql
from django.core.serializers.json import json
from sxrmd import settings

sql_connect = pymysql.connect(host=settings.MYSQL_HOST, port=settings.MYSQL_PORT, user=settings.MYSQL_USER,passwd=settings.MYSQL_PASSWD, db=settings.MYSQL_DBNAME, charset='utf8')
# key='key'
cursor = sql_connect.cursor()


def losecredit(request):
    global cursor
    if request.method == 'GET':
        try:
            cursor.
        except Exception as e:
            print('error')
            # 异常后重连
            print(e)
            sql_connect = pymysql.connect(host=settings.MYSQL_HOST, port=settings.MYSQL_PORT, user=settings.MYSQL_USER,
                                      passwd=settings.MYSQL_PASSWD, db=settings.MYSQL_DBNAME, charset='utf8')
            cursor = sql_connect.cursor()

        name = request.GET.get('name')
        idnum = request.GET.get('idnum')

        if name is None or idnum is None:
            ret = [{'result': '0', 'detail': '输入字段为空'}]
            return JsonResponse(ret, safe=False, json_dumps_params={'ensure_ascii': False})
        colums = ['cidno', 'fname', 'region', 'case_time', 'case_no', 'court', 'basis_no', 'detail', 'fullfil',
                  'publish_time']

        print(name, ' ', idnum)

        if len(name) == 0 or len(idnum) == 0:
            ret = [{'result': '0', 'detail': '输入字段为空'}]
            return JsonResponse(ret, safe=False, json_dumps_params={'ensure_ascii': False})

        name = name.strip()
        idnum = idnum.strip()

        name = name.replace('\'', '')
        idnum = idnum.replace('\'', '')
        # 密文查询
        if len(name) == 32 and len(idnum) == 32:
            # ret = [{'result':'md5密文长度不符合'}]
            # return HttpResponse(json.dumps(ret),content_type='text/json')
            # name = '3486df4a8d4b21cfab42a1f56d52313e'
            # idnum = '3622060fa9d08684b088f8769d8ee5c5'

            resp = []
            cmd1 = "select * from dishonest t where t.fnameGbkMd5='{0}'".format(name)
            cursor.execute(cmd1)
            ret = cursor.fetchall()

            if not ret:
                ret = [{'result': '0', 'detail': '没找到此人'}]
                return JsonResponse(ret, safe=False, json_dumps_params={'ensure_ascii': False})

            for item in ret:
                flag = item[-1]
                # flag 为 1 身份证完整
                if flag == '1':
                    cmd_1 = "select t.fname,t.idNum from dishonest t where t.fnameGbkMd5='{0}' and t.idNumMd5='{1}'".format(
                        name, idnum)
                    cursor.execute(cmd_1)
                    ret2 = cursor.fetchall()

                    for item in ret2:
                        query_name = item[0]
                        query_idnum = item[1]
                        cmd = "SELECT DISTINCT t.cidno,t.fname, t.region, t.case_time, t.case_no, t.court, t.basis_no, t.detail,  t.fullfil, t.publish_time FROM   dw_person_dishonest t where t.fname='{0}' and t.cidno ='{1}'".format(
                            query_name, query_idnum)
                        cursor.execute(cmd)
                        ret3 = cursor.fetchall()
                        d = {}
                        for j in ret3:
                            for index, value in enumerate(j):
                                d[colums[index]] = value
                        resp.append(d)

                    return JsonResponse(resp, safe=False, json_dumps_params={'ensure_ascii': False})
                else:
                    first_of_idnum = int(idnum[0], 16)
                    if first_of_idnum == 0:
                        cmd_2 = "SELECT t.fname,t.idNum FROM dishonest t WHERE t.fnameGbkMd5 = '{0}' AND EXISTS (SELECT  1 FROM  credit t1 WHERE  t1.idNumMd5 = '{1}' AND CONCAT(LEFT(t1.idNum, 4),RIGHT(t1.idNum, 4)) = CONCAT(LEFT(t.idNum, 4),RIGHT(t.idNum, 4)))".format(
                            name, idnum)
                    else:
                        cmd_2 = "SELECT t.fname,t.idNum FROM dishonest t WHERE t.fnameGbkMd5 = '{0}' AND EXISTS (SELECT  1 FROM  credit{1} t1 WHERE  t1.idNumMd5 = '{2}' AND CONCAT(LEFT(t1.idNum, 4),RIGHT(t1.idNum, 4)) = CONCAT(LEFT(t.idNum, 4),RIGHT(t.idNum, 4)))".format(
                            name, first_of_idnum, idnum)

                    cursor.execute(cmd_2)
                    ret2 = cursor.fetchall()
                if ret2:
                    id_set = set()
                    for i in ret2:
                        # print(i)
                        name_decode = i[0]
                        id_set.add(i[1])

                    id_list = list(id_set)
                    query_set = []
                    for i in id_list:
                        query_set.append("\"" + i + "\"")

                    query_sets = ','.join(query_set)

                    cmd_3 = "SELECT DISTINCT t.cidno,t.fname, t.region, t.case_time, t.case_no, t.court, t.basis_no, t.detail,  t.fullfil, t.publish_time FROM   dw_person_dishonest t where  t.fname='{0}' and t.cidno in({1})".format(
                        name_decode, query_sets)
                    cursor.execute(cmd_3)
                    result = cursor.fetchall()

                    for j in result:
                        d = {}
                        for index, value in enumerate(j):
                            d[colums[index]] = value
                        resp.append(d)

                    return JsonResponse(resp, safe=False, json_dumps_params={'ensure_ascii': False})
                else:
                    ret = [{'result': '0'}]
                    return JsonResponse(ret, safe=False, json_dumps_params={'ensure_ascii': False})

        # 明文查询
        else:
            cmd = "SELECT DISTINCT t.cidno,t.fname, t.region, t.case_time, t.case_no, t.court, t.basis_no, t.detail,  t.fullfil, t.publish_time FROM   dw_person_dishonest t where t.fname='{0}' and t.cidno ='{1}'".format(
                name, idnum)

            cursor.execute(cmd)
            ret = cursor.fetchall()
            resp = []

            if ret:
                for j in ret:
                    d = {}
                    for index, value in enumerate(j):
                        d[colums[index]] = value
                    resp.append(d)
            else:
                resp.append({'result': '0'})

            return JsonResponse(resp, safe=False, json_dumps_params={'ensure_ascii': False})