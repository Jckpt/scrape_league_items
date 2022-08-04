from lib2to3.pgen2.literals import simple_escapes
import json
from bs4 import BeautifulSoup
import requests
item = "Abyssal_Scepter_item_HD.webp"
print(item[:item.find("_item")])
url = "https://leagueoflegends.fandom.com/wiki/Guardian_Angel"
result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')
passiveChild = doc.find_all(text="Passive")
statsChild = doc.find_all(text="Stats")
consumeChild = doc.find_all(text="Consume")
try:
    passive = passiveChild[0].parent.parent.div.div.get_text()
except:
    passive = "undefined"
print(passive)
try:
    stats = statsChild[0].parent.parent.find_all("div",{"data-source":True})
    for i, stat in enumerate(stats):
        stats[i] = stat.text.replace('\n',"")
except:
    stats = []
try:
    consume = consumeChild[0].parent.parent.find("div").text.replace('\n',"")
except:
    consume = "undefined"
print(consume)
print(stats)
myJson = {
        'id': '0',
        'name': 'Guardian Angel',
        'alternativeName': [],
        'passive': passive,
        'stats': stats,
        'consume': consume,
        'file': 'Guardian_Angel_item_HD.webp'
    }
with open('items.json', 'w', encoding='utf8') as json_file:
    json.dump(myJson, json_file, ensure_ascii=False)