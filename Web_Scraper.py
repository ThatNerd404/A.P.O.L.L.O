from PySide6.QtCore import QThread, Signal
from newspaper import Article
from duckduckgo_search import DDGS
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
        self.url = "https://html.duckduckgo.com/html/" # DuckDuckGo HTML endpoint
        self.stop_flag = False
        
    def run(self):
        """
        Run the web scraper.
        """
    
        try: 
            if self.stop_flag:
                return
            with DDGS() as ddgs:
                results = ddgs.text(self.query, max_results=1)
                article = Article(results[0]['href'])
                article.download()
                article.parse()
                clean_text = article.text
            
            if self.stop_flag:
                return
           
            self.finished.emit(clean_text)
                
        except Exception as e:
            self.error.emit(e)
            
    def stop(self):
        """
        Stop the web scraper.
        """
        self.stop_flag = True
        self.finished.emit("Web scraping stopped.")

if __name__ == "__main__":

    with DDGS() as ddgs:
        results = ddgs.text("What is the weather in Clarksville Tennessee currently?", max_results=1)
        '''article = Article(results[0]['href'])
        article.download()
        article.parse()
        clean_text = article.text
        print(clean_text)'''
    import trafilatura
    import requests
    headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/114.0.0.0 Safari/537.36"
    )}
    response = requests.get(results[0]['href'], timeout=10, headers=headers)
    print()
    response.raise_for_status()  # Ensure the request was successful
    downloaded = trafilatura.extract(response.text, include_comments=False, include_tables=False)
    print(downloaded)

    # Print the first 500 characters of the article text
    ''' # Example usage
    start_time = time.perf_counter()
    url = "https://html.duckduckgo.com/html/"
    params = {
        "q": "What is the weather in Clarksville, TN currently?",
        #"format": "json",
        #"no_html": 1,
        #"skip_disambig": 1
    }
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.post(url,headers=headers, params=params)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    for link in soup.find_all("a", class_="result__a", limit=1):
        title = link.get_text()
        href = link['href']
        results.append({"title": title, "url": href})
    print(results)
    print(f"Request completed in {time.perf_counter() - start_time:.2f} seconds")'''
    