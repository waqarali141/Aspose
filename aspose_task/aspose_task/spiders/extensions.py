__author__ = 'waqarali'
import urlparse
import copy
from scrapy import Spider, Request
from aspose_task.items import AsposeTaskItem


class Extensions(Spider):
    name = 'extensions'

    def start_requests(self):
        yield Request(url='http://file.org/sitemap.html', callback=self.parse_home_page)

    def parse_home_page(self, response):
        all_extensions = response.css('.page_text a')
        for extension in all_extensions:
            prefix = extension.xpath('text()').extract()[0].strip()
            url = urlparse.urljoin(response.url,
                                   extension.xpath('@href').extract()[0]
                                   )
            yield Request(url=url,
                          callback=self.parse_extensions_over_view,
                          meta={'prefix': prefix})

    def parse_extensions_over_view(self, response):
        for extension_request in self.extract_extensions_listing(response):
            yield extension_request

        if response.xpath('.//*[@class="page_text"]//p[contains(text(), "Page")]//a'):
            for next_page in self.parse_pagination(response):
                yield next_page

    def extract_extensions_listing(self, response):
        listed_extensions = response.xpath('.//*[@class="page_text"]//p[descendant::br]')
        for extension in listed_extensions:
            meta = copy.deepcopy(response.meta)

            name = extension.xpath('.//a/@title').extract()[0].split()[2] .replace('.', '')
            url = urlparse.urljoin(response.url,
                                   extension.xpath('.//a/@href').extract()[0]
                               )
            meta['name'] = name
            yield Request(url=url,
                          callback=self.parse_extension_detail,
                          meta = meta)

    def parse_pagination(self, response):
        next_pages = response.xpath('.//*[@class="page_text"]//p[contains(text(), "Page")]//a[not(contains(text(), "1"))]')
        for page in next_pages:
            meta = copy.deepcopy(response.meta)
            url = page.xpath('@href').extract()[0]
            url = urlparse.urljoin(response.url, url)
            yield Request(url=url,
                          meta=meta,
                          callback=self.extract_extensions_listing)

    def parse_extension_detail(self, response):

        extension_info = response.css('.opening_file >p, h1, .purpose, .software').xpath('.//text()').extract()
        extension_info = self.clean_description(extension_info)
        extension_item = AsposeTaskItem()
        extension_item['name'] = response.meta['name']
        extension_item['prefix'] = response.meta['prefix']
        extension_item['detail'] = extension_info
        yield extension_item

    def clean_description(self, text):
        if isinstance(text, list):
            cleaned_text = list()
            for line in text:
                if line.strip():
                    cleaned_text.append(line.strip())
            return '\n'.join(cleaned_text)
        else:
            return text.strip()




