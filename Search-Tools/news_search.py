from newsapi import NewsApiClient

#Pick your free API key from the official website
newsapi = NewsApiClient(api_key='21cfb08747744647b0bc548294b21b41')



top_headlines = newsapi.get_top_headlines(
    language='en'
)



def news_search(query):
    all_articles = newsapi.get_everything(q=query,
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
    
    results = []
    for title in all_articles['articles'][:10]:
     a = (title['title'],title['url'])
     results.append(a)
    return results



all_articles = news_search("Trump")
print(all_articles)

    
    
#That's everything for 8th aprile hopefully  tomorrow I get more serious and commit whole files instead of snippets.
#I think this two tools are more than enough for a news reader and I'll start a newsrader Agent tommorow.