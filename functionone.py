#this function returns url
from metaphor_python import Metaphor

query='Generative AI'

def get_metaphor_articles(query, num_results=5, include_domains=['www.sciencedirect.com']):
    try:
        api_key = "7cfc68fb-5d3f-42a8-bb5d-3dc310c38f41"
        client = Metaphor(api_key=api_key)
        response = client.search(query, num_results=num_results, include_domains=include_domains)  
        articles = [{"url": result.url} for result in response.results]
        return articles
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
answer=get_metaphor_articles(query)
print(answer)