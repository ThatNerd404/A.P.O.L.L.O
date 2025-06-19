from PySide6.QtCore import QThread, Signal
import trafilatura
import requests
import time
from duckduckgo_search import DDGS
from llama_cpp import Llama
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
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/114.0.0.0 Safari/537.36"
            )}
    def run(self):
        """
        Run the web scraper.
        """
    
        try: 
            if self.stop_flag:
                return
            with DDGS() as ddgs:
                results = ddgs.text(self.query, max_results=1)
                
            response = requests.get(results[0]['href'], timeout=10, headers=self.headers)
            response.raise_for_status()  # Ensure the request was successful
            extracted_data = trafilatura.extract(response.text, include_comments=False, include_tables=False)
            
            if self.stop_flag:
                return
           
            self.finished.emit(extracted_data)
                
        except Exception as e:
            self.error.emit(str(e))
            
    def stop(self):
        """
        Stop the web scraper.
        """
        self.stop_flag = True
        self.finished.emit("Web scraping stopped.")

if __name__ == "__main__":
    start_time = time.perf_counter()
    with DDGS() as ddgs:
        results = ddgs.text("What is the weather in Clarksville Tennessee currently?", max_results=1)

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
    llm = Llama(
                    model_path="Models\mistral-7b-instruct-v0.2-code-ft.Q4_0.gguf",
                    n_ctx= 0, # max context size, zero means use the model's default context size
                    n_threads=6,
                    n_gpu_layers=0,
                    verbose=False # makes the model print out its progress, set to True for only for debugging
                )

    response_text = ""
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"<web search information>{downloaded}</web search information><question>What is the weather in Clarksville, TN currently?</question>"}
    ]
    for chunk in llm.create_chat_completion(messages=messages, stream=True):
        delta = chunk["choices"][0]["delta"].get("content", "")
        response_text += delta
        print(delta, end='', flush=True)

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
    