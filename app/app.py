import gradio as gr
from market_data import process_market_data, get_summary
from plot_utils import plot_normal_distribution
from chatbot import analyze_investment

def market_analysis(ticker, start_date, end_date):
    try:
        # Get market data and calculate metrics
        market_data = process_market_data(ticker, start_date, end_date)
        summary = get_summary(market_data)

        # Plot normal distribution
        graph_path = plot_normal_distribution(market_data)

        # Analyze investment opportunity
        ai_recommendation = analyze_investment(summary)

        # Prepare results
        summary_text = "\n".join([f"{key}: {value}" for key, value in summary.items()])
        return summary_text, ai_recommendation, graph_path

    except Exception as e:
        return f"Error: {str(e)}", None, None

# Create Gradio interface
interface = gr.Interface(
    fn=market_analysis,
    inputs=[
        gr.Textbox(label="Market Ticker (e.g., AAPL)"),
        gr.Textbox(label="Start Date (YYYY-MM-DD)"),
        gr.Textbox(label="End Date (YYYY-MM-DD)")
    ],
    outputs=[
        gr.Textbox(label="Metrics Summary"),
        gr.Markdown(label="Investment Recommendation"),
        gr.Image(label="Normal Distribution Plot")
    ],
    title="AI Market Analysis",
    description="Enter a ticker and date range to analyze the market and get investment recommendations."
)

if __name__ == "__main__":
    interface.launch()