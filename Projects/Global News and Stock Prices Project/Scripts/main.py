import requests
import yfinance as yf
import pandas as pd
import logging
import os

# Logging for better error tracking
logging.basicConfig(level=logging.INFO)

# Function to fetch news data
def fetch_news(api_key, query, num_articles=10):
    """
    Fetches news articles from NewsAPI.
    
    Parameters:
    - api_key (str): Your NewsAPI key.
    - query (str): Query term for fetching news articles.
    - num_articles (int): Number of articles to fetch.
    
    Returns:
    - list: A list of dictionaries containing news articles titles and publication dates.
    """
    url = "https://newsapi.org/v2/everything"
    parameters = {
        "q": query,
        "apiKey": api_key,
        "pageSize": num_articles
    }
    try:
        response = requests.get(url, params=parameters)
        response.raise_for_status() # Raise an exception for HTTP errors 
        data = response.json()
        articles = data.get("articles", [])[:num_articles]
        news_data = [{"title": article["title"], "published_at": article["publishedAt"]} for article in articles]
        return news_data
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching news data: {e}") # Use Logging instead of print 
        return[]

# Function to fetch stock prices
def fetch_stock_data(tickers):
    """
    Fetches stock data from Yahoo Finance.
    
    Parameters:
    - tickers (list): A list of stock tickers.
    
    Returns:
    - dict: A dictionary with stock tickers as keys and their corresponding data.
    """
    stock_data = {}
    try:
        hist = yf.download(tickers, period="1d") # Fetch data for all tickers in one go
        for ticker in tickers:
            if ticker in hist.columns.levels[1]:
                stock_data[ticker] = {
                    "close": hist["Close"][ticker].iloc[0],
                    "volume": hist["Volume"][ticker].iloc[0] if "Volume" in hist.columns else None # Safely handle missing volume
            }
    except Exception as e:
        logging.error(f"Error fetching stock data: {e}") # Use Logging for errors 

    return stock_data

# Modular print functions for better code organization and readability
def print_news(news):
    """
    Prints news data to the console.
    
    Parameters:
    - news (list): List of news articles.
    """
    print("News Data:")
    for article in news:
        print(f"Title: {article['title']}, Published At: {article['published_at']}")

def print_stock_data(stock_data):
    """
    Prints stock data to the console.
    
    Parameters:
    - stock_data (dict): Dictionary containing stock data.
    """
    print("\nStock Data:")
    for ticker, data in stock_data.items():
        close_price = data.get("close", "N/A")
        volume = data.get("volume", "N/A")
        print(f"{ticker} - Close: {close_price}, Volume: {volume}")

# Main function
def main():
    # Get API key from env variables for better security
    news_api_key = os.getenv('NEWS_API_KEY')
    if not news_api_key:
        logging.error("API key is not set. Please set the NEWS_API_KEY environment variable.")
        return
    
    # Fetch news data
    query = "finance"
    news = fetch_news(news_api_key, query)
    print_news(news) # Using modular function to print news

    # Fetch stock prices
    tickers = ["AAPL", "GOOG", "AMZN"]
    stock_data = fetch_stock_data(tickers)
    print_stock_data(stock_data) # Using modular function to print stock data

    # Combine and analyze data
    combined_data = pd.DataFrame(news)
    combined_data["source"] = "News"
    for ticker, data in stock_data.items():
        combined_data = pd.concat([combined_data, pd.DataFrame([{
            "title": f"{ticker} Stock Data",
            "published_at": pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S'), #Improved date format
            "source": "Stocks",
            "close_price": data["close"],
            "volume": data["volume"]
        }])], ignore_index=True)

    # Reset index for better readability in the combined data
    combined_data = combined_data.reset_index(drop=True) # Removed duplicate indexing for readability

    # Rename columns for better presentation
    combined_data.rename(columns={"title": "Title", "published_at": "Published At", "source": "Source"}, inplace=True)
    
    print("\nCombined Data")
    print(combined_data.to_string(index=False)) # Improved readability by removing the index

if __name__ == "__main__":
    main()     
    