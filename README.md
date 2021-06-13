# How to Create and Deploy a Sentiment Analysis App via API

### We use the  model nlptown/bert-base-multilingual-uncased-sentiment. This is a BERT model trained for multilingual sentiment analysis, and which has been contributed to the HuggingFace model repository.

** we have to run the Uvicorn web server which will provide the necessary back end functionality. **

Execute the fast api instance using  the below command 

uvicorn main:app --reload

You will get something like this:

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [16296] using statreload
INFO:     Started server process [8300]
INFO:     Waiting for application startup.
INFO:     Application startup complete.


Open your browser as indicated to http://127.0.0.1:8000 and you should see:

{"message":"This is the sentiment analysis app"}

We can try using the browser address bar to make some requests, by passing value with query string (http://127.0.0.1:8000/sentiment_analysis/?text=" This product is good and cost effective"

After executing the next script (i.e.,rest_request.py) and you should get a result like this:

query = {'text':'i hate this product and would not definitely recommend this to my friends!'}

python rest_request.py

>>> {'sentiment': 'very negative', 'probability': 0.8194750882148743}





