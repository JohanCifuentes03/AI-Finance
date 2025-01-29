import os
import gradio as gr
from dotenv import load_dotenv
from market_data import process_market_data, get_summary
from plot_utils import plot_normal_distribution
from chatbot import analyze_investment

# Load environment variables
load_dotenv()

def market_analysis(ticker, start_date, end_date):
    try:
        # Get market data and calculate metrics
        market_data = process_market_data(ticker, start_date, end_date)
        summary = get_summary(market_data)

        # Plot normal distribution
        graph_path = plot_normal_distribution(market_data)

        # Analyze investment opportunity using OpenAI
        ai_recommendation = analyze_investment(summary)

        # Prepare results
        summary_text = "\n".join([f"{key}: {value}" for key, value in summary.items()])
        return summary_text, ai_recommendation, graph_path

    except Exception as e:
        return f"Error: {str(e)}", None, None

# Create Gradio interface with improved styling
css = """
.gradio-container {
    font-family: 'Arial', sans-serif;
}
.gr-button {
    background-color: #2196F3;
    border: none;
    color: white;
    border-radius: 4px;
}
.gr-button:hover {
    background-color: #1976D2;
}
"""

interface = gr.Interface(
    fn=market_analysis,
    inputs=[
        gr.Textbox(label="Market Ticker (e.g., AAPL)", placeholder="Enter ticker symbol"),
        gr.Textbox(label="Start Date", placeholder="YYYY-MM-DD"),
        gr.Textbox(label="End Date", placeholder="YYYY-MM-DD")
    ],
    outputs=[
        gr.Textbox(label="Metrics Summary"),
        gr.Markdown(label="Investment Recommendation"),
        gr.Image(label="Normal Distribution Plot")
    ],
    title="📈 AI Market Analysis",
    description="Get professional market analysis and AI-powered investment recommendations.",
    theme="default",
    css=css
)

if __name__ == "__main__":
    interface.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False
    )