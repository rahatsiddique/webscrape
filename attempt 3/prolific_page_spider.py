#in the terminal write the following:
#scrapy shell
#fetch(""https://blog.prolific.ac/")
# if you want to check view(response)
# print(response.text)

#to extract the article title do the following:

#response.css("h2 a ::text").extract_first()

#note: if you want to make sure that you don't return any other h2 that might have different info write: response.css(.post-title a ::text").extract_first()

fetch("https://blog.prolific.ac/")

