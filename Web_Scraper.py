from PySide6.QtCore import QObject, QThread










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