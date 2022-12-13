import requests

#facts = requests.get("https://theaxolotlapi.netlify.app/").json()
#print(facts.get("facts"))

pic = requests.get("https://theaxolotlapi.netlify.app/").json()
print(pic)