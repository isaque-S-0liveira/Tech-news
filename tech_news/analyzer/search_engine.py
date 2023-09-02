from tech_news.database import db


# Requisito 7
def search_by_title(title):
    regex_pattern = f".*{title}.*"
    query = {"title": {"$regex": regex_pattern, "$options": "i"}}
    news = db.news.find(query)
    result = [(news_item["title"], news_item["url"]) for news_item in news]

    return result


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
