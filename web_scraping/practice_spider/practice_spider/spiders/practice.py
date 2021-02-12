import scrapy


class PracticeSpider(scrapy.Spider):
  name = 'practice'
  allowed_domains = ['books.toscrape.com']
  start_urls = ['http://books.toscrape.com/']

  def parse(self, response):
    test = response.xpath('//*[@class="col-sm-8 h1"]/*/text()').extract()

    yield {'Test': test}
