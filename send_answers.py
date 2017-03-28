#Script que imprime en un servidor local el cuestionario en formato json.
import json 
import requests 
with open('introduction_quiz.json') as json_quiz:
	data = json.load(json_quiz)

response = requests.post('http://localhost:9200/data/carlos/11?pretty', json = data)
print(response.text)
