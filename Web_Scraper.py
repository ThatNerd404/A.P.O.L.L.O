from PySide6.QtCore import QThread, Signal
import time
import requests
from bs4 import BeautifulSoup
""" Web Scraper for APOLLO
    This script is designed to scrape web pages for specific content and summarize it using a pre-trained model from hugging face.
    It uses the PySide6 library for the user interface and the transformers library for text summarization.
"""

class WebScraper(QThread):
    """
    WebScraper class for scraping web pages and summarizing content.
    
    Attributes:
        url (str): The URL of the web page to scrape.
        summary (str): The summarized content of the web page.
    """
    finished = Signal(str)
    error = Signal(str)
    
    def __init__(self, query):
        """
        Initialize the WebScraper with a query.
        
        Args:
            query (str): The search query to use for scraping.
        """
        super().__init__()
        self.query = query
        self.url = "https://api.duckduckgo.com/"
        self.stop_flag = False
        
    def run(self):
        """
        Run the web scraper.
        """
        params = {
        "q": self.query,
        "format": "json",
        "no_html": 1,
        "skip_disambig": 1
    }
        try: 
            if self.stop_flag:
                return
            response = requests.get(self.url, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            if self.stop_flag:
                return
            abstract_text = data.get("AbstractText", "No instant answer found.")
            self.finished.emit(abstract_text)
                
        except requests.RequestException as e:
            self.error.emit(f"Request failed: {str(e)}")
            
    def stop(self):
        """
        Stop the web scraper.
        """
        self.stop_flag = True
        self.finished.emit("Web scraping stopped.")
        
if __name__ == "__main__":
    # Example usage
    start_time = time.perf_counter()
    url = "https://api.duckduckgo.com/"
    params = {
        "q": "Who is ada lovelace?",
        "format": "json",
        "no_html": 1,
        "skip_disambig": 1
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(f"Raw data received: {data}")
    print(data.get("AbstractText", "No instant answer found.")) 
    # AbstractText is the key for the instant answer and second option is the fallback if it doesn't exist
    print(f"Request completed in {time.perf_counter() - start_time:.2f} seconds")
