import requests
from bs4 import BeautifulSoup
import json


def fetch_news_articles(base_url, article_selector, title_selector, link_selector):
    response = requests.get(base_url)
    print("response : ", response)
    json_string = json.dumps(response.json(), indent=2)
    print(json_string)

    if response.status_code != 200:
        print("Failed to fetch the page.")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.select(article_selector)

    news_data = []
    for article in articles:
        title = article.select_one(title_selector)
        link = article.select_one(link_selector)

        if title and link:
            news_data.append(
                {
                    "title": title.get_text(strip=True),
                    "link": (
                        link["href"]
                        if "http" in link["href"]
                        else base_url + link["href"]
                    ),
                }
            )

    return news_data


# Example usage for BBC News
if __name__ == "__main__":
    BASE_URL = "https://www.bbc.com/news"
    ARTICLE_SELECTOR = ".gs-c-promo"  # Adjust this based on the site's HTML structure
    TITLE_SELECTOR = ".gs-c-promo-heading__title"
    LINK_SELECTOR = "a.gs-c-promo-heading"

    articles = fetch_news_articles(
        BASE_URL, ARTICLE_SELECTOR, TITLE_SELECTOR, LINK_SELECTOR
    )
    print("articles : ", articles)
    for i, article in enumerate(articles, 1):
        print(f"{i}. {article['title']}")
        print(f"   {article['link']}")
