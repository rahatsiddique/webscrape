import scrapy

class PageSpider(scrapy.Spider):
    name = "page"
    start_urls = ["https://blog.prolific.ac/"]

    def parse(self, response):
        for article_url in response.css('h2 a ::attr("href")').extract():
            yield response.follow(article_url, callback=self.parse_article)
        older_posts = response.css('.nav-previous a ::attr("href")').extract_first()
        if older_posts is not None:
            yield response.follow(older_posts, callback=self.parse)

    def parse_article(self, response):
        content = response.css("h1::text").extract()
        yield {"article": "".join(content)}


#in the command line write 'scrapy crawl page' because it is the name attribute