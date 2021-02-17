from bs4 import BeautifulSoup
import requests

start = 0

i = 0
while i < 5:
    i += 1

    url = f'https://onlinecasinobox.net/={start}&count=10&search_descriptions=0&sort_column=popular&sort_dir=desc&appid=730'
    rs = requests.get(url)

    html = rs.json()['results_html']
    root = BeautifulSoup(html, "html.parser")

    for a in root.select('.market_listing_row_link'):
        print(a["href"])

    print('\n' + '-' * 100 + '\n')

    start += 10
