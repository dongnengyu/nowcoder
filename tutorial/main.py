from scrapy import cmdline

#主方法，调用scrapy crawl dmoz

if __name__=="__main__":
    cmdline.execute("scrapy crawl dmoz".split())