import scrapy

class MultiPageSpider(scrapy.Spider):
    name = "multi_page"
    start_urls = ["https://blog.prolific.ac/"]

    def parse(self, response):
        for article_url in response.css('h2 a ::attr("href")').extract():
            author = response.css('span a ::attr("href")').extract()
            date = response.css('span time ::attr("datetime")').extract()

            article = response.follow(article_url, callback=self.parse_article)
            yield {"article": article, "author": author, "date": date}

        older_posts = response.css('.nav-previous a ::attr("href")').extract_first()
        if older_posts is not None:
            yield response.follow(older_posts, callback=self.parse)

    def parse_article(self, response):
        content = response.css("h1::text").extract()
        yield "".join(content)



#in the command line write 'scrapy crawl page' because it is the name attribute