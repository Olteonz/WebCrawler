import requests
from bs4 import BeautifulSoup as bs
import threading


def spider(articles):
    """
    Spider function crawls on the page of TheVerge to find links to articles and print the titles of first 10 articles
    to the console. The crawling on specific articles is multithreaded

    :param articles: int (the number of articles to save links of)
    :return: list of strings (links to articles)
    """

    article_links = []
    page = 1
    while len(article_links) < articles:
        url = 'https://www.theverge.com/games/archives/'+str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = bs(plain_text, features="html.parser")

        for article_link in soup.findAll('h2', class_="c-entry-box--compact__title"):
            link = article_link.find('a')
            article_links.append(link.get('href'))
            if len(article_links) >= articles:
                break
        page += 1

    thread0 = threading.Thread(target=spider_thread(article_links[0]))
    thread0.start()
    thread1 = threading.Thread(target=spider_thread(article_links[1]))
    thread1.start()
    thread2 = threading.Thread(target=spider_thread(article_links[2]))
    thread2.start()
    thread3 = threading.Thread(target=spider_thread(article_links[3]))
    thread3.start()
    thread4 = threading.Thread(target=spider_thread(article_links[4]))
    thread4.start()
    thread5 = threading.Thread(target=spider_thread(article_links[5]))
    thread5.start()
    thread6 = threading.Thread(target=spider_thread(article_links[6]))
    thread6.start()
    thread7 = threading.Thread(target=spider_thread(article_links[7]))
    thread7.start()
    thread8 = threading.Thread(target=spider_thread(article_links[8]))
    thread8.start()
    thread9 = threading.Thread(target=spider_thread(article_links[9]))
    thread9.start()

    thread0.join()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()

    return article_links


def spider_thread(link):
    """
    spider_thread function prints the title of a TheVerge article

    :param link: string (link to article to extract title from)
    :return: none
    """
    article_soup = bs(requests.get(link).text, features="html.parser")
    text = article_soup.find('h1', class_="c-page-title").getText()
    print(text)


print(spider.__doc__)
print(spider(10))