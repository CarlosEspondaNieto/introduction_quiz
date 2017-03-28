# introduction_quiz version 1.0
## Repo for Jorge quiz
### The introduction_json runs with elasticsearch
> Requirements:
* elasticsearch
* python3.6

> Instructions:
* Install elasticsearch: `sudo yum install elasticsearch`

* Create virtualenv into repo:
  `virtualenv -p python3.6 env`
  
* activate virtualenv: `source env/bin/activate`
    
* install libraries requests and json:
  `pip install requests`
  
  `pip install simplejson`
 
* run the send_answer.json file: `python send_answer.py`

* write the url in a browser to see the quiz: `http://localhost:9200/data/carlos/11?pretty` 
 
