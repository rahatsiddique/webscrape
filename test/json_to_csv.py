import csv

import json

#want to split this into methods/classes so that it explains what I'm doing

def write_json_to_csv(json):
    with open('page_collect.csv', 'w+') as csvfile:
        numberwriter = csv.writer(csvfile)
        titles = 'article titles'
        numberwriter.writerow([titles])

        for item in json:
            page_collect = item ['article_url']
            print(page_collect)
            numberwriter.writerow([page_collect])

def open_json_file(file_name):
    from pprint import pprint

    with open(file_name) as f:
        data = json.load(f)

    write_json_to_csv(data)

open_json_file('../data/page_collect.json')

#the following is hardcoded
#write_json_to_csv([
#{"article_url": "/curious-at-prolific-rare-insights-the-tech-minds-behind-prolific/"},
#{"article_url": "/representative-samples-are-coming-soon/"}
#])