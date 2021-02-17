
import re

import urllib

import requests



sitemap = 'https://onlinecasinobox.net/sitemap.xml'



html = urllib.request.urlopen(sitemap).read().decode('utf-8')

result = re.findall(re.compile(r'(?<=<loc>).*?(?=</loc>)'), html)



with open('all_links_sitemap.txt', 'w') as file:

  for data in result:

    print(data, file=file)

file.close()