baseUrl = ("http://api.meituan.com/group/v4/deal/select/city/94/cate/1?"
                "sort=solds&hasGroup=true&mpt_cate1=1&offset={0}&limit={1}")
i=0
limit=25
url=baseUrl.format(str(i*limit),limit)
print(url)