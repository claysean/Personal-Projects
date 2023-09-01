import requests
from bs4 import BeautifulSoup

def get_spell_description(spell_name):
    base_url = "https://2e.aonprd.com"
    spell_url = f"{base_url}/Spells.aspx?ID={spell_name.replace(' ', '%20')}"
    
    response = requests.get(spell_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        description = soup.find("p", class_="spell-description").get_text()
        return description
    else:
        return None

spell_name = input("Enter the name of the spell: ")
description = get_spell_description(spell_name)

if description:
    print(description)
else:
    print("Spell not found or error occurred.")