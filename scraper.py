import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

def scrape_news(company):
    search_url = f"https://www.bing.com/news/search?q={company}&FORM=HDRSC6"

    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(search_url, headers=headers)

        if response.status_code != 200:
            logging.error(f"Failed to fetch news. Status: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("a", class_="title")

        news_list = []
        for article in articles[:10]:
            title = article.text.strip()
            link = article["href"]
            news_list.append({"title": title, "content": link})

        return news_list

    except Exception as e:
        logging.error(f"Error scraping: {e}")
        return []


