# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
class DaomuPipeline(object):
    def process_item(self, item, spider):
        directory = 'D:/novel/{}/'.format(item['title'])
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = directory + item['name'] + '.txt'
        with open(filename,'w',encoding='utf-8') as f:
            f.write(item['content'])
        return item
