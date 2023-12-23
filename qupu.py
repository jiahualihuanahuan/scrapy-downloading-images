import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from piano.items import PianoItem

class QupuSpider(CrawlSpider):
    name = "qupu"
    allowed_domains = ["meitu131.com","ertuba.com"]
    start_urls = ["https://www.meitu131.com/meinv"]

    rules = (
        # Rule(LinkExtractor(allow=r"meinv"), ),
        # Rule(LinkExtractor(allow=r"gangqin", deny=r"video"), ),
        Rule(LinkExtractor(allow=r"meinv/[0-9]{1,8}"), callback="parse_item", follow=True),
            )

    def parse_item(self, response):
        image_urls = response.css('div.work-content').css('img::attr(src)').extract()
        # image_urls = response.urljoin(image_urls)
        item = PianoItem() 
        item['image_urls'] = image_urls
        yield item 
