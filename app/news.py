import requests
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()
api_key = os.getenv("RAPID_API_KEY")

def get_news(tickers, max_news=5, max_chars=2000):
    """
    Obtiene y formatea noticias del mercado desde Yahoo Finance, limitando la cantidad y caracteres.

    Parámetros:
    - tickers (str): Símbolo(s) del mercado (ej. "AAPL").
    - max_news (int): Máximo de noticias a obtener (por defecto, 5).
    - max_chars (int): Máximo de caracteres en el texto final (por defecto, 2000).

    Retorna:
    - str: Noticias formateadas, limitadas en cantidad y caracteres.
    """
    if not api_key:
        raise ValueError("La clave de API no está configurada. Verifica tu archivo .env")

    url = "https://yahoo-finance15.p.rapidapi.com/api/v2/markets/news"
    headers = {
        "x-rapidapi-host": "yahoo-finance15.p.rapidapi.com",
        "x-rapidapi-key": api_key
    }
    querystring = {"tickers": tickers, "type": "ALL"}

    try:
        response = requests.get(url, params=querystring, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Asegurar que "body" está en la respuesta y es una lista
        news_list = data.get("body", [])
        if not isinstance(news_list, list) or len(news_list) == 0:
            return "No hay noticias disponibles en este momento."

        # Filtrar las primeras `max_news` noticias
        limited_news = news_list[:max_news]

        # Construir el texto de salida con límite de caracteres
        news_text = ""
        for news in limited_news:
            title = news.get("title", "Sin título")
            link = news.get("url", "No disponible")
            date = news.get("time", "Fecha no disponible")
            source = news.get("source", "Fuente desconocida")
            summary = news.get("text", "Sin resumen disponible")

            # Agregar noticia formateada
            news_text += f"📰 **{title}** ({source})\n"
            news_text += f"📅 {date}\n"
            news_text += f"🔗 [Leer más]({link})\n"
            news_text += f"📖 {summary}\n\n"

            # Detener si se supera el límite de caracteres
            if len(news_text) >= max_chars:
                break  

        return news_text[:max_chars]  # Asegurar que el texto final no exceda el límite

    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud a la API: {e}")
        return "Error al obtener las noticias."