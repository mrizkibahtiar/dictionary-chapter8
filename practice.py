import requests # type: ignore

api_key = "865c3231-fb9d-4b1e-a628-da9b698661ae"
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)
definitions = res.json()
print(definitions)

for definition in definitions:
    print(definition)