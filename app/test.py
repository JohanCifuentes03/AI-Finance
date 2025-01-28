from market_data import process_market_data, get_summary
from plot_utils import plot_normal_distribution
from scraping_utils import get_market_news
from chatbot import analyze_investment

def test_app():
    # 1. Configuración inicial
    ticker = "AAPL"  # Cambia este ticker según lo necesites
    start_date = "2020-01-01"
    end_date = "2023-01-01"

    try:
        # 2. Procesar datos del mercado
        print("\nDescargando datos...")
        market_data = process_market_data(ticker, start_date, end_date)
        print(f"Datos descargados para {ticker}:\n{market_data.head()}")

        # 3. Calcular métricas del mercado
        print("\nCalculando métricas...")
        summary = get_summary(market_data)
        print(f"Resumen de métricas:\n{summary}")

        # 4. Generar gráfica de distribución normal
        print("\nGenerando gráfica de distribución normal...")
        graph_path = plot_normal_distribution(market_data)
        print(f"Gráfica guardada en: {graph_path}")

        # 5. Realizar scraping de noticias
        print("\nObteniendo noticias relevantes...")
        news = get_market_news(ticker)
        print("Noticias relevantes:")
        for headline in news:
            print(f"- {headline}")
        
        # 6. Consultar al chatbot
        print("\nConsultando al chatbot para recomendación de inversión...")
        news_summary = "\n".join(news)
        ai_recommendation = analyze_investment(summary, news_summary)
        print("\nRecomendación del Chatbot:")
        print(ai_recommendation)

    except Exception as e:
        print(f"\nOcurrió un error: {str(e)}")
