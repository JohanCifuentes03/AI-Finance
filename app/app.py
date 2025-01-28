import gradio as gr
from market_data import process_market_data, get_summary
from plot_utils import plot_normal_distribution
from scraping_utils import get_market_news
from chatbot import analyze_investment

def market_analysis(ticker, start_date, end_date):
    try:
        # Obtener datos del mercado y calcular métricas
        market_data = process_market_data(ticker, start_date, end_date)
        summary = get_summary(market_data)

        # Graficar distribución normal
        graph_path = plot_normal_distribution(market_data)

        # Obtener noticias relevantes
        news = get_market_news(ticker)
        news_summary = "\n".join(news)

        # Analizar si es conveniente invertir
        ai_recommendation = analyze_investment(summary, news_summary)

        # Preparar resultados
        summary_text = "\n".join([f"{key}: {value}" for key, value in summary.items()])
        return summary_text, news_summary, ai_recommendation, graph_path

    except Exception as e:
        return f"Error: {str(e)}", None, None, None

# Crear interfaz Gradio
interface = gr.Interface(
    fn=market_analysis,
    inputs=[
        gr.Textbox(label="Ticker del mercado (ej: AAPL)"),
        gr.Textbox(label="Fecha de inicio (YYYY-MM-DD)"),
        gr.Textbox(label="Fecha de fin (YYYY-MM-DD)")
    ],
    outputs=[
        gr.Textbox(label="Resumen de métricas"),
        gr.Textbox(label="Noticias relevantes"),
        gr.Markdown(label="Recomendación de inversión"),
        gr.Image(label="Gráfica de la distribución normal")
    ],
    title="Análisis del Mercado con IA",
    description="Ingresa un ticker y un rango de fechas para analizar el mercado, ver noticias y obtener recomendaciones de inversión."
)

if __name__ == "__main__":
    interface.launch()
