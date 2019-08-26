from scrapy import cmdline
cmdline.execute("scrapy crawl votedoctor -s LOG_FILE=all.log".split())
