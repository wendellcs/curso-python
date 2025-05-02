import re

text = '''
Olá! Recentemente, encontrei alguns recursos muito úteis que gostaria de compartilhar com você. Por exemplo, se você está interessado em aprender programação, pode conferir https://www.codecademy.com ou https://freecodecamp.org.
Além disso, se está procurando notícias de tecnologia, recomendo visitar https://www.theverge.com e https://techcrunch.com. Ambos são excelentes para se manter atualizado.
Caso esteja planejando sua próxima viagem, https://www.booking.com e https://www.airbnb.com são ótimos para hospedagem. Não se esqueça de checar os reviews em https://www.tripadvisor.com.
Ah, e para compras online, há sempre https://www.amazon.com e https://www.ebay.com. Espero que esses links sejam úteis!
'''

def get_url(txt):
    pattern = r'http[s]?:\/\/(?:www\.)?[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})(?:\/[^\s]*)?'
    urls = re.findall(pattern, txt)
    
    print(f'\nWe have found {len(urls)} urls in the text:\n')
    for url in urls:
        print(f'---> {url}\n')
        

get_url(text)