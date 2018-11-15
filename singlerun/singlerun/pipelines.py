# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class SinglerunPipeline(object):
    def process_item(self, item, spider):
        self.numberwriter.writerow([item["article"]])|''
        return item

    def open_spider(self,spider):
        self.file= open('file2.csv', 'w', encoding = "utf-16")
        self.numberwriter = csv.writer(self.file, dialect="excel-tab")
        self.numberwriter.writerow(["article titles", "author", "date"])


    def close_spider(self, spider):
        self.file.close()


#utf-16 works with the excel on my laptop, in general this can be utf-8 but doens't work for excel for mac :(