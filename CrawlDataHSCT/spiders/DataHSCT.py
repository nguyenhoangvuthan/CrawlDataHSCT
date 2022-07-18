import scrapy

from CrawlDataHSCT.items import CrawldatahsctItem


class DatahsctSpider(scrapy.Spider):
    name = 'DataHSCT'
    allowed_domains = ['hosocongty.vn']
    start_urls = ['https://hosocongty.vn/thang-06/2022-ho-chi-minh/page-%s' % page for page in range(1,235)]

    def parse(self, response):
        items = CrawldatahsctItem()
        companies_name = response.xpath('//ul[@class="hsdn"]/li/h3/a/text()').extract()
        companies_code = response.xpath('//ul[@class="hsdn"]/li/div/a/text()').extract()

        information_companies = zip(companies_name, companies_code)

        for information_company in information_companies:
            items['company_name'] = information_company[0],
            items['company_code'] = information_company[1]

            yield items

        # next_page = response.xpath('//div[@class="next_page"]/a/@href').get()
        # if next_page:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)