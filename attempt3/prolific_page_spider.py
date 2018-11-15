#in the terminal write the following:
#scrapy shell
#fetch(""https://blog.prolific.ac/")
# if you want to check view(response)
# print(response.text)

#to extract the article title do the following:

#response.css("h2 a ::text").extract_first()

#note: if you want to make sure that you don't return any other h2 that might have different info write: response.css("h2.post-title a ::text").extract_first()

#to extract the author name do the following:
#response.css("span.post-meta a ::text").extract()

#to extract the date write the following:
#response.css("span.post-meta time ::text").extract()



