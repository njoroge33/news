from app import app
from .models import Source, Article
import requests

api_key = app.config['NEWS_API_KEY']

def get_sources():
    url = f"https://newsapi.org/v2/sources?apiKey={api_key}"
    url_data = requests.get(url)
    url_data_dict = url_data.json()
    sources_list = url_data_dict['sources']

    return process_sources(sources_list)

def process_sources(sources_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects according to objects
    '''
    sources = []
    for source in sources_list:
        source = Source(source['id'], source['name'], source['description'],
                        source['url'], source['category'], source['language'], source['country'])
        sources.append(source)
    return sources
