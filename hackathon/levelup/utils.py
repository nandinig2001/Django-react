from transformers import pipeline

# Initialize the summarization pipeline
summarizer = pipeline("summarization")

def generate_summary(text):
    summary = summarizer(text, max_length=500, min_length=25, do_sample=False)
    return summary[0]['summary_text']