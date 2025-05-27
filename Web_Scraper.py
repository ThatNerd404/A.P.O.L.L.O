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
        #self.url = 
        
    def run(self):
        """
        Run the web scraper.
        """
        pass
    
    





from transformers import pipeline

def summarize_text(text):
    """
    Summarizes the input text using a pre-trained model.
    
    Args:
        text (str): The text to summarize.
    
    Returns:
        str: The summarized text.
    """
    # Load the summarization pipeline with a pre-trained model
    # You can choose a different model if needed
    summarizer = pipeline("summarization",  framework="pt")
    trimmed_text = text[:1024]
    summary = summarizer(trimmed_text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    # Example usage
    # This is just a placeholder. You can replace it with actual web scraping logic.
    example_text = """
    A big percentage of so-called experts today only know how to configure tools, but they understand nothing about how things work at the deeper level. This is a real challenge and a big problem for the future.

A steering wheel is an abstraction that makes it easier for me to drive my car. Power steering is yet another level of abstraction that further improves the driving experience. Abstractions are nice, they generally improve the quality of life. However, in Denmark we have a proverb that says:

    Too little and too much spoils everything.

What good does an abstraction do when it breaks and nobody any longer understand how the technology works under the hood?

Everything in the tech industry is driven with a very hardcore eye for profit and very little interest in anything else. So you need to be able to push out new products or new services as fast as possible. This means more abstraction and more automation, less and less people, and less deeper understanding.

Today programmers and system administrators no longer exist, instead we have DevOps and even DevSecOps, in which the industry is trying very hard to stuff every single task into the job description of a single individual. The tech guys needs to do development (Dev), security (Sec) and operations (Ops), i.e. system administration, but since no single individual can truly master all that, we need to automate as much as possible in order to save money and avoid the complexities of human social interaction between different tech departments. As a result, the modern tech person is only taught about how to use specific tools, he or she then knows very little about the technology under the hood.

It doesn't help that technology has become increasingly difficult to understand, but more and more of modern life depend heavily upon the tech we're using. So what is going to happen when the level of understanding in the tech industry reaches such a low point in which the majority of people don't even know how to fix the tools they are using?

"Manual scene" from the WALL-E movie.

People have become accustomed to the state of abstraction and they think it's the correct approach and they happily contribute to the mess by adding even more abstraction.

    Yes, let's all go back to coding in assembly!

    ― Sarcastic comment by arrogant developer

We need abstractions, no doubt about it, but every level of abstraction comes with a heavy price which, ironically enough, eventually can cause a massive loss in profit.

    Modern programming scares me in many respects, where they will just build layer after layer after layer that does nothing except translate.

    ― Ken Thompson

Already now a majority of "security people" know very little about security and only about how to use some kind of pre-made penetration testing tool. The penetration testing tool shows a bunch of green lights in its web GUI board and all is assumed well. Yet, a real security expert with evil intentions has broken the system long ago and keeps selling valuable data on the darknet. Nothing is leaked and nothing is discovered. This can go on for years without anyone finding out because, well, the GUI board says that all is OK.

Some students today apparently don't even know what files and folders are. """
    # grab start time
    start_time = time.perf_counter()
    # Summarize the example text
    summary = summarize_text(example_text)
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Time taken to summarize: {total_time:.2f} seconds")
    # Print the summary
    print("Original Text:", example_text)
    print("Summarized Text:", summary)
    
