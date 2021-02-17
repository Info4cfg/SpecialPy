from requests_html import HTMLSession
session = HTMLSession()
r = session.get('https://onlinecasinobox.net/sitemap/')
r.html.absolute_links 
{'https://onlinecasinobox.net/sitemap/'}
with open("файл.txt", "w") as file:
    print(r.html.absolute_links, file=file)
