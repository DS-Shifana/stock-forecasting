import yfinance as yf
import os

def download_stock_data(ticker, start_date, end_date, interval='1d', save_path='data/raw/'):
    df = yf.download(ticker, start=start_date, end=end_date, interval=interval)
    
    # Create directory if not exists
    os.makedirs(save_path, exist_ok=True)
    
    # Save to CSV
    file_name = f"{ticker}_{interval}.csv"
    df.to_csv(os.path.join(save_path, file_name))
    print(f"Data for {ticker} saved to {os.path.join(save_path, file_name)}")

if __name__ == "__main__":
    download_stock_data(
        ticker="AAPL",               # Example: Apple stock
        start_date="2020-01-01",
        end_date="2024-12-31",
        interval="1d"
    )
