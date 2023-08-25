# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnalysisItem(scrapy.Item):
    title=scrapy.Field()
    jobs_title=scrapy.Field()
    company_name=scrapy.Field()
    Location=scrapy.Field()
    Required_skills=scrapy.Field()
    views=scrapy.Field()
    Deadline=scrapy.Field()

