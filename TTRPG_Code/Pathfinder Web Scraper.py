import bs4 as bs
import requests

mURL = "https://pf2.d20pfsrd.com/monster/"
r = requests.get(mURL)
print(r.content)