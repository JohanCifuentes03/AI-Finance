import pandas as pd
import yfinance as yf

def process_market_data(ticker, start_date, end_date):
    """
    Descarga los datos históricos del mercado desde Yahoo Finance.
    """
    data = yf.download(ticker, start=start_date, end=end_date)

    # Verificar si los datos están vacíos
    if data.empty:
        raise ValueError(f"No se encontraron datos para el ticker {ticker} entre {start_date} y {end_date}.")

    # Aplanar índices (remover niveles adicionales como 'Ticker')
    if isinstance(data.columns, pd.MultiIndex):
        data = data.stack().reset_index(level=1, drop=True)  # Deja solo las columnas principales

    return data.reset_index()


def get_summary(market_data):
    """
    Calcula las métricas principales de los datos del mercado.
    """
    median_price = market_data['Close'].median()
    min_price = market_data['Close'].min()
    max_price = market_data['Close'].max()
    current_price = market_data['Close'].iloc[-1]

    summary = {
        "Mediana": round(median_price, 2),
        "Mínimo": round(min_price, 2),
        "Máximo": round(max_price, 2),
        "Precio actual": round(current_price, 2)
    }

    return summary
