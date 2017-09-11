# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AsposeTaskPipeline(object):
    # To save the scrapped item as a Django Model Object in DB
    def process_item(self, item, spider):
        item.save()
        return item
