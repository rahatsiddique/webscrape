import scrapy

class PageSpider(scrapy.Spider):
    name = "page"
    start_urls = ["https://blog.prolific.ac/"]

    def parse(self, response):
        for article_url in response.xpath('.//div[@class="post-title"]/descendant::text()').extract():
            yield {"article_url": article_url}
           # yield response.follow(article_url, callback=self.parse_article)



    def parse_article(self, response):
        content = response.xpath('.//div[@class="entry-content"]/descendant::text()').extract()
        yield {"article": "".join(content)}


#previously used response.cc('.post-title a ::attr("href")')