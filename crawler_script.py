from billiard.context import Process
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class CrawlerScript:
    def __init__(self, settings=None):
        if settings is None:
            settings = get_project_settings()
        self.crawler = CrawlerProcess(settings)

    def _crawl(self):
        self.crawler.start()
        self.crawler.stop()

    def crawl(self, spider_cls, *args, **kwargs):
        self.crawler.crawl(spider_cls, *args, **kwargs)

    def run(self):
        p = Process(target=self._crawl)
        p.start()
        p.join()

