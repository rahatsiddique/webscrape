import json

with open('blog.json') as blog_file:
    data = json.load(blog_file)
    for blog in data:
        print(blog['article'])


        #print(blog) will print all text


    #print(data[0]['article']) - this would print a single article. to do all articles use a for loop

    #print(json.load(blog_file))

    #print(blog_file.read())