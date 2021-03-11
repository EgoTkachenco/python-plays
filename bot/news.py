import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

BASE_URL = 'https://www.bbc.com/'
CATEGORIES = ['coronavirus', 'world', 'business',
              'technology', 'science_and_environment']


def loadTopNews(category):
    url = BASE_URL + 'news/' + category
    html = urllib.request.urlopen(BASE_URL + 'news/' + category).read()
    soup = BeautifulSoup(html, 'html.parser')

    articles = []
    for article in soup.find_all('div', class_="gs-c-promo")[1:6]:
        title = article.find('h3').text.rstrip()
        url = article.find('a', class_="gs-c-promo-heading").get('href', None)
        content = article.find('p', class_="gs-c-promo-summary").text.rstrip()
        articles.append(
            {'title': title, 'content': content, 'url': BASE_URL + url})
    return articles


def loadNews(category):
    url = BASE_URL + 'news/' + category
    # Load category page
    html = urllib.request.urlopen(BASE_URL + 'news/' + category).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieav all of the anchor tags
    tags = soup('a')
    # Find valid article urls from page header
    articles_url = []
    for tag in tags:
        if tag.get('class') is not None and 'gs-c-promo-heading' in tag.get('class'):
            post_url = tag.get('href', None)
            if post_url is not None and post_url.startswith('/news'):
                articles_url.append(post_url)
    
    articles = []
    for article_url in articles_url[1:5]:
        articles.append(loadArticle(article_url))
    return articles
    

def loadArticle(url):
    html = urllib.request.urlopen(BASE_URL + url).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Get title and Content
    article = {'content': '', 'title': ''}
    article['title'] = soup('h1')[0].text
    contents = soup('div')
    for content in contents:
        if content.get('class', None) is not None and 'ssrcss-uf6wea-RichTextComponentWrapper' in content.get('class', None):
            article['content'] += content.text + '\n'
    return article

