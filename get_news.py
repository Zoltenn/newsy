import requests, os

def search(keyword: str):
    '''
    KEYWORD: search term for returning news stories on the keyword topic
    '''

    base_url = 'https://newsapi.org/v2'
    endpoint = '/everything'
    keyword = '?q=' + keyword

    # token into request header
    token = open(os.path.expanduser('~\\Documents\\token.txt')).read()
    headers = {'Authorization': token}
    
    url = base_url + endpoint + keyword
    r = requests.get(url, headers=headers)

    # TODO: handle content formatting

    return r.json()
