from newsapi import NewsApiClient

#Pick your free API key from the official website
newsapi = NewsApiClient(api_key='')

# /v2/top-headlines
#top_headlines = newsapi.get_top_headlines(country='jp')

top_headlines = newsapi.get_top_headlines(
    language='en'
)

# /v2/everything
#all_articles = newsapi.get_everything(q='bitcoin',
#                                      sources='bbc-news,the-verge',
#                                      domains='bbc.co.uk,techcrunch.com',
#                                      from_param='2017-12-01',
#                                      to='2017-12-12',
#                                      language='en',
#                                      sort_by='relevancy',
#                                      page=2)
#
## /v2/top-headlines/sources
#sources = newsapi.get_sources()

for title in top_headlines['articles'][:10]:
    print(title['title'],title['url'])