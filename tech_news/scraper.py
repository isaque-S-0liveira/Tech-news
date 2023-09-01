from parsel import Selector
import requests
import time
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    news_url = selector.css(".entry-title a::attr(href)").getall()
    if not news_url:
        return []
    return news_url


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css("a.next.page-numbers::attr(href)").get()
    if not next_page:
        return None
    return next_page


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    url = selector.css('link[rel="canonical"]::attr(href)').get()
    title = selector.css(".entry-title::text").get().strip()
    author = selector.css(".author a::text").get()
    timestamp = selector.css("li.meta-date::text").get()
    reading_time = selector.css(".meta-reading-time::text").get()
    summary = "".join(
        selector.css(".entry-content > p:first-of-type *::text").getall()
    ).strip()
    category = selector.css(".category-style .label::text").get()

    if not title:
        return {"url": None, "title": None, "timestamp": None, "writer": None}
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": author,
        "reading_time": int(reading_time[:2]),
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    URL_BASE = "https://blog.betrybe.com/"
    resonse_html = fetch(URL_BASE)
    links = []
    news = []

    while amount > len(links):
        links.extend(scrape_updates(resonse_html))
        next_page = scrape_next_page_link(resonse_html)
        resonse_html = fetch(next_page)

    for url in links[:amount]:
        news_html = fetch(url)
        news.append(scrape_news(news_html))
    print(news, len(news))
    create_news(news)
    return news


get_tech_news(5)
