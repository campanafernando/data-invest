# data-invest

This Python project uses Streamlit to build an interactive dashboard that displays stock market data. Data comes from `yfinance` for near real-time stock information, while `pydantic` handles data modeling.

Install Poetry and run the following command to download the dependencies:

```sh
poetry install
```

Start the dashboard with:

```sh
streamlit run main.py
```

This opens the dashboard in your default browser.

Choose an asset and a time range to view its historical data.

The data is shown in interactive charts to support analysis. The dashboard also displays detailed information about the selected assets.
