import os
import requests
from bs4 import BeautifulSoup
import trafilatura
from dotenv import load_dotenv
from serpapi import GoogleSearch



api ="your serp api key"





def search_web(query , count=10):
    url = "https://serpapi.com/search"
    params={
    "engine" : "google",
    "q": "latest tech news",
    "api_key": api,

    "hl": "en",
    "gl": "us"
    }
    response = requests.get(url , params=params )
    response.raise_for_status()
    data = response.json()
    results = data.get("organic_results", [])
    return [item["link"] for item in results[:count]]

def scrape_url(url):
    try:
        download = trafilatura.fetch_url(url)
        text = trafilatura.extract(download)
        if text:
            return text
        else:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.get_text()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")

        return None
