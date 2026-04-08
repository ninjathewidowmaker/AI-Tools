from newsapi import NewsApiClient

#Pick your free API key from the official website
newsapi = NewsApiClient(api_key='')



top_headlines = newsapi.get_top_headlines(
    language='en'
)



def news_search(query):
    all_articles = newsapi.get_everything(q=query,
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
    
    return all_articles

# /v2/top-headlines/sources
#sources = newsapi.get_sources()

#all_articles = news_search("Trump")

all_articles = news_search("Trump")

for title in all_articles['articles'][:10]:
    print(title['title'],title['url'])
    
    
