import requests

#facts = requests.get("https://dog-api.kinduff.com/api/facts").json()
#print(facts.get("facts"))

pic = requests.get("https://theaxolotlapi.netlify.app/").json()
print(pic)