from tech_news.database import db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    regex_pattern = f".*{title}.*"
    query = {"title": {"$regex": regex_pattern, "$options": "i"}}
    news = db.news.find(query)
    result = [(news_item["title"], news_item["url"]) for news_item in news]

    return result


# Requisito 8
def search_by_date(date):
    try:
        # Converter a data para o formato dd/mm/AAAA
        formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )
        query = {"timestamp": formatted_date}
        news = db.news.find(query)
        result = [(news_item["title"], news_item["url"]) for news_item in news]

        return result if result else []
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    try:
        query = {"category": {"$regex": category, "$options": "i"}}
        news = db.news.find(query)

        result = [(news_item["title"], news_item["url"]) for news_item in news]

        return result if result else []
    except Exception as error:
        raise error
