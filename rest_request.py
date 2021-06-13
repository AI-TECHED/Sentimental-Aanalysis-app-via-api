import requests

query = {'text':'i hate this product and would not definitely recommend this to my friends!'}
response = requests.get('http://127.0.0.1:8000/sentiment_analysis/', params=query)
print(response.json())