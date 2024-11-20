# Global News and Stock Prices Project

This project combines news articles and stock price data to provide a consolidated view of both types of information. It fetches the latest news related to finance and the current stock prices of popular tickers (such as AAPL, GOOG, and AMZN). The final output is a combined dataset containing both the news and stock data for easy analysis.

## Features
- Fetches the latest finance-related news articles using the News API.
- Retrieves stock price data for a list of tickers using Yahoo Finance.
- Combines news and stock data into a single dataset for further analysis.
- Outputs the consolidated data to the console and saves it to a CSV file.

## Requirements
To run this project, the following packages need to be installed:

- `requests` - to make HTTP requests to the News API.
- `yfinance` - to retrieve stock price data.
- `pandas` - to handle data manipulation and storage.

You can install all dependencies using the following command:

```sh
pip install requests yfinance pandas
```

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/global-news-stock-project.git
   cd global-news-stock-project
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Setup
1. **News API Key**: To run this project, you need a News API key. Sign up at [https://newsapi.org](https://newsapi.org) to obtain your key.

2. **Environment Variables**: Set up the `NEWS_API_KEY` environment variable to store your API key securely. You can do this by running:
   - On **Windows**:
     ```sh
     set NEWS_API_KEY=your_api_key_here
     ```
   - On **macOS/Linux**:
     ```sh
     export NEWS_API_KEY=your_api_key_here
     ```

## Usage
Run the script using the following command:

```sh
python main.py
```

The script will:
- Fetch the latest finance-related news articles.
- Fetch the stock price data for tickers: AAPL, GOOG, AMZN.
- Print the combined data to the console.
- Save the combined data to a CSV file named `combined_data.csv`.

## Project Structure
- `main.py` - The main script that runs the project.
- `requirements.txt` - Contains the list of dependencies needed for this project.
- `combined_data.csv` - Output file containing the combined news and stock data.

## Example Output
The script will output the combined data to the console as well as save it to `combined_data.csv`. Here's an example:

```
Title                                                               Published At           Source    close_price      volume
Trump’s crypto website crashed after its token...                 2024-10-15 22:17:14    News              NaN          NaN
Treasury must compensate Scotland for tax hike...                  2024-10-31 10:35:55    News              NaN          NaN
Trumpcoin Launches With a Whimper                                  2024-10-16 13:53:23    News              NaN          NaN
UK borrowing for September third highest on record                 2024-10-22 06:12:15    News              NaN          NaN
Harris says Irish general election to be called on Friday          2024-11-06 19:28:33    News              NaN          NaN
Is AI the Answer to Your Money Problems? Here's What It Can...     2024-10-16 12:00:46    News              NaN          NaN
AAPL Stock Data                                                    2024-11-14 17:15:02    Stocks     228.220001  43401721.0
GOOG Stock Data                                                    2024-11-14 17:15:02    Stocks     177.350006  16716910.0
```

## Notes
- Ensure that you do **not** push your API keys to public repositories. It is recommended to store them securely using environment variables.
- If you mistakenly push an API key, consider revoking it immediately and generating a new one.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions
Feel free to submit a pull request if you want to add features or improve the project. Contributions are always welcome!

## Contact
For any questions or issues, please reach out to [your-email@example.com](mailto:your-email@example.com).

