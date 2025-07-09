# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class EcommercePipeline:
    def process_item(self, item, spider):
        
        #print(item["rating"].split(" ")[1])
        rating =item["rating"]
        
        temp=rating.split(" ")[1]
        if temp=="One":
            item["rating"]=1
        if temp=="Two":
            item["rating"]=2
        if temp=="Three":
            item["rating"]=3
        if temp=="Four":
            item["rating"]=4
        if temp=="Five":
            item["rating"]=5
        return item
