import json
import time
from urllib import request

MAX_PRICE_DOLLARS = 0.25

def get_cards():
    url = get_download_uri()
    return fetch_json(url)

def get_download_uri():
    url = 'https://api.scryfall.com/bulk-data/default-cards'
    j = fetch_json(url)
    return j.get('download_uri')

def fetch_json(url):
    print(f'Fetching {url} …')
    time.sleep(0.1)
    f = request.urlopen(url)
    print('… fetched …')
    s = f.read()
    print('… read …')
    j = json.loads(s)
    print('… parsed …')
    return j

def main():
    cs = get_cards()
    for c in cs:
        if c.get('legalities', {}).get('commander') != 'legal':
            continue
        tix = c.get('prices', {}).get('usd')
        tix = float(tix) if tix else tix
        legal = tix is not None and tix <= MAX_PRICE_DOLLARS
        prefix = 'Not ' if not legal else ''
        print(f"{c.get('name')}: {prefix}Legal ({tix})")

main()
