# -*- coding: utf-8 -*-
import scrapy
import json
import time
import os.path

class OrphSpider(scrapy.Spider):
    name = 'orph'
    start_urls = ['https://www.orpha.net/consor/cgi-bin/Disease_ProEncyclo_List.php?lng=FR&TAG=T']
        
    headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    

    def parse(self, response):
        urls = response.xpath('//ul[@class="alphabet"]/li/a/@href').extract()
        with open ('check.txt', 'r') as to_check:
            lst = to_check.readlines()
        
        for url in urls:
            url = 'https://www.orpha.net/consor/cgi-bin/' + url.strip()
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_item, headers=self.headers)
            # time.sleep(60)
            
    
    def parse_item(self, response):
        links = response.xpath('//ul/li/ul[@class="articleListDisease"]/li/a/@href').extract()
        for link in links:
            link = 'https://www.orpha.net/consor/cgi-bin/'+link
            yield scrapy.Request(url=link, headers=self.headers, callback=self.parse_article)
            
    def parse_article(self, response):
        article = []
        title = response.xpath('//*[@id="ContentType"]/h2[3]/text()').extract_first()
        definition = response.xpath('//div[@class="definition"]/section/p/text()').extract_first()
        online_date = response.xpath('//*[@id="ContentType"]/div/p[@class="author"]/strong[2]/text()').extract_first()
        url = response.url
        article.append(title)
        article.append(definition)
        article.append(online_date)
        article.append(url)
        
        
        with open('data.txt', 'a') as f:
            f.writelines(json.dumps(article))
            f.write('\n')