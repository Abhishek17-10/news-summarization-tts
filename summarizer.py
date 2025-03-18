from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_text(text):
    """Summarizes long news articles."""
    if len(text.split()) < 50:
        return text  # Return as is if too short
    
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']
