from urllib.parse import urlparse


#Get Domain Name

def get_domain_name(url):
    try:
        results=get_sub_Domain_name(url).split('.')
        return results[-2]  + '.' + results[-1]
    except:
        return ''
def get_sub_Domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
