import json
batch = []
with open('data.txt', 'r') as f:
    for line in f.readlines():
        batch.append(json.loads(line))
        
        
for line in batch:
    with open ('check.txt', 'a') as f:
        if line[2] == None:
            f.writelines(line[3]+ '\n')
            
            

    article = []
    title = response.xpath('//*[@id="ContentType"]/h2[3]/text()').extract_first()
    definition = response.xpath('//div[@class="definition"]/section/p/text()').extract_first()
    online_date = response.xpath('//*[@id="ContentType"]/div/p[@class="author"]/strong[2]/text()').extract_first()
    url = response.url
    article.append(title)
    article.append(definition)
    article.append(online_date)
    article.append(url)
    time.sleep(2)
    
    
    with open('data.txt', 'a') as f:
        f.writelines(json.dumps(article))
        f.write('\n')