import scrapy

"""
categories = $x('//div[@class="sidebar-nav navbar-collapse"]/ul[@class="nav"]/li/a/text()').map(x => x.wholeText)
titles = $x('(//div[@class="thumbnail"]/div[@class="caption"]/h4/a/@title)').map(x =>x.value)
price = $x('//div[@class="thumbnail"]/div[@class="caption"]/h4[1]/text()').map(x => x.wholeText)
description = $x('//div[@class="thumbnail"]/div[@class="caption"]/p/text()').map(x => x.wholeText)
images = $x('//div[@class="thumbnail"]/img/@src').map(x => x.value)
reviews = $x('//div[@class="thumbnail"]/div[@class="ratings"]/p[1]/text()').map(x => x.wholeText)
ratings = $x('//div[@class="thumbnail"]/div[@class="ratings"]/p/@data-rating').map(x => x.value)
href = $x('//*[@id="side-menu"]/li[2]/a/@href').map(x =>x.value)

"""
class AllinoneSpider(scrapy.Spider):
    name = 'allinone'
    # allowed_domains = ['https://webscraper.io']
    start_urls = ['https://webscraper.io/test-sites/e-commerce/allinone/']
    
    custom_settings = {
        'FEED_URI': 'products.csv',
        'FEED_FORMAT': 'csv',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        urls = [
            'https://webscraper.io/test-sites/e-commerc',
            'https://webscraper.io/test-sites/e-commerce/allinonee/allinone/computers',
            'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops',
            'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets',
            'https://webscraper.io/test-sites/e-commerce/allinone/phones',
            'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'
            ]        
        # categories = response.xpath('//div[@class="sidebar-nav navbar-collapse"]/ul[@class="nav"]/li/a/text()')
        #         
        for i in urls:
            yield response.follow(i, callback=self.parse_products)
        

    def parse_products(self, response):
    
        categorie = response.xpath('//div[@class="col-md-9"]/h1/text()').get()
        titles = response.xpath('//div[@class="thumbnail"]/div[@class="caption"]/h4/a/@title').getall()
        price = response.xpath('//div[@class="thumbnail"]/div[@class="caption"]/h4[1]/text()').getall()
        description = response.xpath('//div[@class="thumbnail"]/div[@class="caption"]/p/text()').getall()
        images = response.xpath('//div[@class="thumbnail"]/img/@src').getall()
        reviews = response.xpath('//div[@class="thumbnail"]/div[@class="ratings"]/p[1]/text()').getall()
        ratings = response.xpath('//div[@class="thumbnail"]/div[@class="ratings"]/p/@data-rating').getall()

        yield{
            categorie:{
                'titles': titles,
                'price' : price,
                'description': description,
                'images' : images,
                'reviews' : reviews,
                'ratings' : ratings
            }
            
        }
