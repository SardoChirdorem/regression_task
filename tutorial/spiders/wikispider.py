import scrapy
import os


class wikispider(scrapy.Spider):
    name = "wiki"

    def start_requests(self):
        urls = [
            "https://en.wikipedia.org/wiki/ABBA"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-3]
        filename = f"{page}.txt"
        os.remove(r"C:\Users\mrdas\scrapy\tutorial\tutorial\spiders\en.wikipedia.org.txt")
        for para in response.xpath("//div[@class='mw-parser-output']/p"):
            text = para.xpath("string(.)").getall()
            with open(filename, "a", encoding="utf-8") as f:
                f.write(text[0].strip())
        self.log(f"Saved file: {filename}")
