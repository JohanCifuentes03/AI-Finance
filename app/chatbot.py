from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key= os.getenv("OPENAI_API_KEY")

openai = OpenAI(api_key=api_key)


def analyze_investment(summary):
    """
    Utiliza un modelo de lenguaje para analizar si es conveniente invertir basándose en métricas y noticias.
    """
    prompt = f"""
    Eres un asesor financiero de inteligencia artificial. Tu tarea es analizar los datos históricos del mercado, noticias recientes, 
    y proporcionar una recomendación sobre si es conveniente invertir.

    Me vas a dar la información en formato Markdown.

    Resumen del mercado:
    - Mediana: {summary['Mediana']}
    - Mínimo: {summary['Mínimo']}
    - Máximo: {summary['Máximo']}
    - Precio actual: {summary['Precio actual']}
    """

    response = openai.chat.completions.create(
        model="gpt-4o-mini", 
        messages=[
            {"role":"system", "content":prompt},
            {"role": "user", "content":"¿Debería invertir en este mercado?"}
        ]
    )
    return response.choices[0].message.content
