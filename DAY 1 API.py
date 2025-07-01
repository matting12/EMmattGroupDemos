import requests
import json


BASE_URL = "http://localhost:3000"

response = requests.get(f"{BASE_URL}/city/Springfield")


json_response = response.json()

stat_json = json_response['statistics']
demo_json = stat_json['demographics']
education_json = demo_json['education']
high_school_graduate = education_json['high_school_graduate']


my_dict = {'about' : 'me', "lorem": "ipsum"}


print(stat_json[0])
