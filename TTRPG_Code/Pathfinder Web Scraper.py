import bs4 as bs
import requests

URL = "https://pf2.d20pfsrd.com/monster/"
r = requests.get(URL)
print(r.content)