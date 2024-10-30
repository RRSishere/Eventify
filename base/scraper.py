# scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_links_from_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    h4_tags = soup.find_all('h4')
    links = []

    for h4 in h4_tags:
        a_tag = h4.find('a')
        if a_tag:
            name = a_tag.text.strip()
            href = a_tag.get('href')
            date = None
            date_span = h4.find_next('span', class_='_webdate')
            if date_span:
                date = date_span.text.strip()
            else:
                p_tag = h4.find_next('p', class_='clearfix')
                if p_tag:
                    span_block = p_tag.find('span', class_='block')
                    if span_block:
                        date = span_block.text.strip()
            links.append({'name': name, 'href': href, 'date': date})

    return links
