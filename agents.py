# agent.py
from search import search_web, scrape_url
from summarize import summarize_text

def research_topic(query):
    urls = search_web(query)
    all_summaries = []
    for url in urls:
        content = scrape_url(url)
        if content and not content.startswith("Error"):
            summary = summarize_text(content)
            all_summaries.append({"url": url, "summary": summary})
    return all_summaries
