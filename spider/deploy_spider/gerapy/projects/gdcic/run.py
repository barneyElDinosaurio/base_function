from scrapy import cmdline

name = 'gdcicbad'  #
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())