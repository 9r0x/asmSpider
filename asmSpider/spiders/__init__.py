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

class proxylistSpider(scrapy.Spider):
    name = "proxylist"
    start_urls = [
        "https://free-proxy-list.net/",
    ]
    def parse(self, response):
        for li in response.css('tbody tr'):
            yield {
                'Ip': li.css('td::text')[0].extract(),
                'Port': li.css('td::text')[1].extract(),
                'Code': li.css('td::text')[2].extract(),
                'Country': li.css('td::text')[3].extract(),
                'Anonymity': li.css('td::text')[4].extract(),
                'Google': li.css('td::text')[5].extract(),
                'Https': li.css('td::text')[6].extract(),
                'Last Checked': li.css('td::text')[7].extract(),
            }
