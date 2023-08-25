import scrapy
from ..items import AnalysisItem 

class analysisSpider(scrapy.Spider):
    name = "analysis"
    start_urls = ["https://merojob.com/category/it-telecommunication/"]

    def parse(self, response):
        # Extract job details
        job_cards = response.css(".card-body")
        for card in job_cards:
            item = AnalysisItem()
            item['jobs_title'] = card.css(".text-primary>a::text").extract()
            item["company_name"] = card.css(".h6>a::text").extract()
            item["Location"] = card.css("span[itemprop='addressLocality']::text").extract()
            item["Required_skills"] = card.css("span[itemprop='skills'] span::text").extract()
            
            yield item

        # Extract footer details
        footer_rows = response.css(".card-footer")
        for row in footer_rows:
            footer_item = AnalysisItem()  # Create a new item instance for footer details
            footer_item['Deadline'] = row.css("span.icon-time span::text").extract()
            footer_item["views"] = row.css("span.text-primary::text").extract()
            
            yield footer_item
