import scrapy

class PageSpider(scrapy.Spider):
    name = "page"
    start_urls = ["https://blog.prolific.ac/"]

    def parse(self, response):
        for article_url in response.css('.post-title a ::attr("href")').extract():
            yield {"article_url": article_url}
           # yield response.follow(article_url, callback=self.parse_article)



    def parse_article(self, response):
        content = response.xpath('.//div[@class="entry-content"]/descendant::text()').extract()
        yield {"article": "".join(content)}


#previously used response.ccs('.post-title a ::attr("href")')