import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.baoquangbinh.vn/kinh-te/202210/ngan-chan-hanh-vi-gian-lan-thuong-mai-dien-tu-2203947/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = response.xpath("//div[@class='col-md-8 mb-5']/h2[@id='title']").get()
        content = response.xpath("//div[@class='col-md-8 mb-5']/div[2]/div[1]/strong").extract_first().strip()
        day = response.xpath("//div[@class='col-md-8 mb-5']/div[@class='d-flex justify-content-between align-items-end page-detail-meta mb-3']/ul[@class='list-unstyled list-inline mb-0']/li[@class='list-inline-item']").get()
        print('tieu de', title)
        print('content', content)
        print('day', day)