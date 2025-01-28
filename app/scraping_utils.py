import requests
from bs4 import BeautifulSoup

def get_market_news(query):
    """
    Realiza scraping en Google News para buscar noticias sobre un mercado específico.
    """
    url = f"https://www.google.com/search?q={query}+stock+news"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraer titulares de noticias
    articles = soup.find_all('h3')  # Google muestra titulares en h3
    headlines = [article.get_text() for article in articles[:5]]  # Limitar a los 5 primeros
    return headlines


data = get_market_news("AAPL")
print(data)