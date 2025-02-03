from openai import OpenAI
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

# Inicializar cliente de OpenAI
openai = OpenAI(api_key=openai_key)

def summarize_market_news(news):
    """
    Resumen de las noticias del mercado usando IA.
    """
    prompt = f"""
    Eres un analista financiero experto en mercados bursátiles. 
    Tu tarea es leer las siguientes noticias y generar un resumen conciso, resaltando:
    
    - Tendencias generales del mercado.
    - Noticias positivas y negativas más relevantes.
    - Factores clave que pueden influir en inversiones.

    Debes devolver solo el resumen en formato Markdown, sin comentarios adicionales. también, si tienes una noticia muy importante adjunta el link, para poder 
    leer más sobre ella.

    **Noticias del mercado:**  
    {news}
    """

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}]
    )
    return response.choices[0].message.content

def analyze_investment(summary, market_data):
    """
    Analiza si es conveniente invertir con base en métricas y tendencias.
    """
    prompt = f"""
    Eres un asesor financiero con más de 10 años de experiencia.  
    Tu tarea es analizar el mercado basándote en estos datos históricos y el resumen de noticias recientes.

    Datos del mercado
    - Mediana: {market_data['Mediana']}
    - Mínimo: {market_data['Mínimo']}
    - Máximo: {market_data['Máximo']}
    - Precio actual: {market_data['Precio actual']}

    Resumen de noticias  
    {summary}

    Tarea
    - Evalúa si es buen momento para invertir.
    - Analiza el sentimiento del mercado según las noticias.
    - Considera la estrategia:  
      - "Atacar cuando todos están asustados."  
      - "Ser precavido cuando todos están eufóricos."  
    - Proporciona una conclusión clara y si es posible justifica el paso a paso de los detalles de tu analisis.
    

    Devuelve la respuesta en formato Markdown con encabezados bien estructurados.
    """

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}]
    )
    return response.choices[0].message.content
