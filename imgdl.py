import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from image.items import ImageItem

class ImgdlSpider(CrawlSpider):
    name = "imgdl"
    allowed_domains = ["meitu131.com","ertuba.com"]
    start_urls = ["https://www.meitu131.com/meinv"]

    rules = (
        Rule(LinkExtractor(allow=r"meinv/[0-9]{1,8}"), callback="parse_item", follow=True),
            )

    def parse_item(self, response):
        image_urls = response.css('div.work-content').css('img::attr(src)').extract()
        # image_urls = response.urljoin(image_urls)
        item = ImageItem() 
        item['image_urls'] = image_urls
        yield item 
