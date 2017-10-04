import scrapy


class MangaLinkSpider(scrapy.Spider):
    name = "mangalink"
    baseLink = 'https://asmhentai.com'
    start_urls = [
        baseLink
    ]

    def parse(self, response, baseLink=baseLink):
        for image in response.css('div.preview_item'):
            yield {
                'title': image.css('div.caption a::text').extract_first(),
                'link': baseLink+image.css('div.image a::attr(href)').extract_first(),
                'thumbnail': 'https:'+image.css('div.image img::attr(src)').extract_first(),
            }

        next_page = baseLink+'/pag/'+str(int(response.css('span.current::text').extract_first())+1)+'/'
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


class VCBSpider(scrapy.Spider):
    name = "vcb"
    baseLink = 'https://vcb-s.com/' 
    start_urls = [
        baseLink
    ]

    def parse(self, response, baseLink=baseLink):
        for image in response.css('div.preview_item'):
            yield {
                'title': image.css('div.caption a::text').extract_first(),
                'link': baseLink+image.css('div.image a::attr(href)').extract_first(),
                'thumbnail': 'https:'+image.css('div.image img::attr(src)').extract_first(),
            }

        next_page = baseLink+'/pag/'+str(int(response.css('span.current::text').extract_first())+1)+'/'
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
