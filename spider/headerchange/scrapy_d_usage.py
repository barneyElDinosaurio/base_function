from scrapyd_api import ScrapydAPI
scrapyd = ScrapydAPI('http://127.0.0.1:6800')
scrapyd.list_jobs('project_name')