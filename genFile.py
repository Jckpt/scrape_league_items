from lib2to3.pgen2.literals import simple_escapes
import json
from bs4 import BeautifulSoup
import requests
import os
data = {"item": [

]}
items = os.listdir('./Old items')
for i, scuffedName in enumerate(items):
    item = scuffedName[:scuffedName.find("_item")]
    itemName = item.replace('_',' ').replace('%27','\'').replace('%28','(').replace('%29',')')
    url = f"https://leagueoflegends.fandom.com/wiki/{item}"
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')
    passiveChild = doc.find_all(text="Passive")
    statsChild = doc.find_all(text="Stats")
    consumeChild = doc.find_all(text="Consume")
    activeChild = doc.find_all(text="Active")
    try:
        passive = passiveChild[0].parent.parent.div.div.get_text()
    except:
        passive = "undefined"
    try:
        stats = statsChild[0].parent.parent.find_all("div",{"data-source":True})
        for j, stat in enumerate(stats):
            stats[j] = stat.text.replace('\n',"")
    except:
        stats = []
    try:
        consume = consumeChild[0].parent.parent.find("div").text.replace('\n',"")
    except:
        consume = "undefined"
    try:
        active = activeChild[0].parent.parent.find("div").text.replace('\n',"")
    except:
        active = "undefined"
    #print(passive)
    #print(stats)
    #print(consume)
    alternativeNames = []
    if "'s" in itemName:
        alternativeNames.append(itemName.replace("'s",""))
        alternativeNames.append(itemName.replace("'",""))
    fullItem = {
            'id': i,
            'name': itemName,
            'alternativeName': alternativeNames,
            'active': active,
            'passive': passive,
            'stats': stats,
            'consume': consume,
            'file': scuffedName
        }
    data['item'].append(fullItem)
    if passive=="undefined" and len(stats)==0 and consume=="undefined":
        print(fullItem)
with open('items.json', 'w', encoding='utf8') as jsonFile:
    json.dump(data, jsonFile, ensure_ascii=False, indent=2)