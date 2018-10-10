import csv

#want to split this into methods/classes so that it explains what I'm doing

def write_json_to_csv(json):
    with open('page_collect.csv', 'w+') as csvfile:
        numberwriter = csv.writer(csvfile)
        title
        for item in json:
            page_collect = item ['article_url']
            print(page_collect)
            numberwriter.writerow([page_collect])




write_json_to_csv([
{"article_url": "/curious-at-prolific-rare-insights-the-tech-minds-behind-prolific/"},
{"article_url": "/representative-samples-are-coming-soon/"}
])