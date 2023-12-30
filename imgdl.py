import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from image.items import ImageItem

class ImgdlSpider(CrawlSpider):
    name = "imgdl" # this is the name of the spider/crawler
    allowed_domains = ["meitu131.com","ertuba.com"] # this is the allowed domains this crawler can access, you can remove this line if you want to explore all linked webpages
    start_urls = ["https://www.meitu131.com/meinv"] # the starting url

    rules = (
        Rule(LinkExtractor(allow=r"meinv/[0-9]{1,8}", deny=r"shouji"), callback="parse_item", follow=True), 
        # in the rules section, the crawler will extract all links that follow the rule but only once.
        # please make sure the rule is built in a way which can fullfill you requirements
        # r"" is regular expression
        # allow is to only go to the url (extract links) which follow the regular expression
        # deny is not go to the url which follow the regular expression
        # callback is that if the link satisfy condition (allow and deny) then go to the function and perform specific scraping function
        # follow means if you wish to extract all links from this url
            )

    def parse_item(self, response):
        image_urls = response.css('div.work-content').css('img::attr(src)').extract()
        # image_urls = response.urljoin(image_urls)
        item = ImageItem() 
        item['image_urls'] = image_urls
        yield item 
