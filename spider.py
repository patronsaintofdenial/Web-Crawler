from urllib.request import urlopen
from link_finder import LinkFinder
from domain import *
from general import *

class Spider :
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

def __init__(self, project_name, base_url, domain_name):
    Spider.project_name = project_name
    Spider.base_url = base_url
    Spider.domain_name = domain_name
    Spider.queue_file = Spider.project_name + '/queue.txt'
    Spider.crawled_file = Spider.project_name + '/crawled.txt'
    self.boot()
    self.crawl_page('First Spider', Spider.base_url)

def crawl_page(thread_name, page_url):
    if page_url not in Spider.Crawled:
        print(thread_name+ ' not crawling ' + page_url)
        print('Queue ' + str(len(Spider.queue)) + ' | Crawled  ' + str(len(Spider.crawled)))
        Spider.add_links_to_queue(Spider.gather_links(page_url))
        Spider.queue.remove(page_url)
        Spider.crawled.add(page_url)
        Spider.update_files()


def gether_links(page_url):
    html_string=''
    try:
        response=urlopen(page_url)
        if 'text/html' in response.getheader('Content-type'):
            html_bytes=response.read()
            html_string=html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
    except Exception as e:
        print(str(e))
        return set()
    return finder.page_links()

def add_links_to_queue(links):
    for url in links:
        if (url in Spider.queue) or (url in Spider.crawled):
            continue
        if Spider.domain_name != get_domain_name(url):
            continue
    Spider.queue.add(url)
def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
