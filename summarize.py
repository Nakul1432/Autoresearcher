from transformers import pipeline

summariser = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_words=150):
    if not isinstance(text, str):
        raise TypeError(f"Expected text to be str, got {type(text).__name__}")

    max_length = int(max_words * 1.5)
    min_length = int(max_words * 0.5)

  
    max_chunk_chars = 3000  
    if len(text) > max_chunk_chars:
        chunks = [text[i:i+max_chunk_chars] for i in range(0, len(text), max_chunk_chars)]
        summaries = []
        for chunk in chunks:
            summary = summariser(
                chunk,
                max_length=max_length,
                min_length=min_length,
                do_sample=False
            )[0]['summary_text']
            summaries.append(summary)
       
        final_summary = summariser(
            " ".join(summaries),
            max_length=max_length,
            min_length=min_length,
            do_sample=False
        )[0]['summary_text']
        return final_summary

    else:
        summary = summariser(
            text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False
        )[0]['summary_text']
        return summary
