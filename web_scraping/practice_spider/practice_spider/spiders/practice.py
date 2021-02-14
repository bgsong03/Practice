import scrapy
import pytest

class PracticeSpider(scrapy.Spider):
  name = 'practice'
  allowed_domains = ['books.toscrape.com']
  start_urls = ['http://books.toscrape.com/']

  def parse(self, response):
    books = response.xpath('//h3/a/@href').extract()
    for urls in books:
      absolute_book_url = response.urljoin(urls)
      yield{'URLS': absolute_book_url}

    next_page_url = response.xpath('//a[text()="next"]/@href').extract_first()
    absolute_next_page_url = response.urljoin(next_page_url)
    yield scrapy.Request(absolute_next_page_url)