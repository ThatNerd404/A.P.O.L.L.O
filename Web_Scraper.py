from PySide6.QtCore import QObject, Signal
""" Web Scraper for APOLLO
    This script is designed to scrape web pages for specific content and summarize it using a pre-trained model from hugging face.
    It uses the PySide6 library for the user interface and the transformers library for text summarization.
"""

class WebScraper(QObject):
    """
    WebScraper class for scraping web pages and summarizing content.
    
    Attributes:
        url (str): The URL of the web page to scrape.
        summary (str): The summarized content of the web page.
    """
    
    
    
    





from transformers import pipeline

def summarize_text(text, max_words=300):
    """
    Summarizes the input text using a pre-trained model.
    
    Args:
        text (str): The text to summarize.
    
    Returns:
        str: The summarized text.
    """
    # Load the summarization pipeline with a pre-trained model
    # You can choose a different model if needed
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    trimmed_text = text[:1024]
    summary = summarizer(trimmed_text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']