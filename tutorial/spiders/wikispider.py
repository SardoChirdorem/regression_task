import scrapy
import os


class wikispider(scrapy.Spider):
    name = "wiki"

    def start_requests(self):
        urls = [
            "https://en.wikipedia.org/wiki/philosophy"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = f"{page}.txt"

        if os.path.exists(fr"c:\users\mrdas\scrapy\data\{filename}"):
            os.remove(fr"C:\Users\mrdas\scrapy\data\{filename}")

        for para in response.xpath("//div[@class='mw-parser-output']/p"):
            text = para.xpath("string(.)").getall()
            with open(fr"c:\users\mrdas\scrapy\data\{filename}", "a", encoding="utf-8") as f:
                f.write(text[0].strip())

        try:
            next_page = response.xpath("//div[@class='mw-parser-output']//p/a")
            for el in next_page:
                ur = el.xpath("string(./@href)").getall()
                the_url = ur[0]
                the_url = response.urljoin(the_url)
                yield scrapy.Request(the_url, callback=self.parse)

        except:
            pass

        self.log(f"Saved file: {filename}")
