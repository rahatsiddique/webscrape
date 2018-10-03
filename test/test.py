import scrapy
class ArticleSpider(scrapy.Spider):
    name = "artile"
    start_urls = ["https://blog.theodo.fr/2018/02/scrape-websites-5-minutes-scrapy/"]

    def parse(self, response):
        content = response.xpath(".//div[@class='entry-content']/descendant::text()").extract()
        yield {'article': ''.join(content)}

