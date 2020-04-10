import requests
import json
import random
from API_KEY import *

FileData=open("___DataBase___.py","a+")

def callApi(url, data, tokenKey):
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + tokenKey,
        'Cache-Control': "no-cache"
    }
    response = requests.request("POST", url, data=data.encode("utf-8"), headers=headers)
    return response.text

def NLP_Offence(Text):       #F+    F       A
    baseUrl = "http://api.text-mining.ir/api/"
    url = baseUrl + "Token/GetToken"
    querystring = {"apikey":random.choice(Keys)}
    response = requests.request("GET", url, params=querystring)
    data = json.loads(response.text)
    tokenKey = data['token']
    #Lets cut the BullShit : )
    url =  baseUrl + "TextRefinement/SwearWordTagger"
    payload = u'"'+Text+'"'
    result = json.loads(callApi(url, payload, tokenKey))
    ## for item in result: ...
    result= (list(result.values()))
    if "StrongSwearWord" in result:
        return "F+"
    elif "MildSwearWord" in result:
        return "F"
    else:
        return "A"

def NLP_POS_Tagger(Text):
    baseUrl = "http://api.text-mining.ir/api/"
    url = baseUrl + "Token/GetToken"
    querystring = {"apikey":random.choice(Keys)}
    response = requests.request("GET", url, params=querystring)
    data = json.loads(response.text)
    tokenKey = data['token']
    url =  baseUrl + "PosTagger/GetPos"
    payload = u'"'+Text+'"'
    result = json.loads(callApi(url, payload, tokenKey))
    Dic={}
    for phrase in result:
        Key=phrase['word']
        Value=phrase['tags']['POS']['item1']
        if Key not in Dic:
            Dic[Key]=[]
        Dic[Key].append(Value)
    return Dic  

def NLP_Ner(Text):
    baseUrl = "http://api.text-mining.ir/api/"
    url = baseUrl + "Token/GetToken"
    querystring = {"apikey":random.choice(Keys)}
    response = requests.request("GET", url, params=querystring)
    data = json.loads(response.text)
    tokenKey = data['token']

    url =  baseUrl + "NamedEntityRecognition/Detect"
    payload = u'"'+Text+'"'
    result = json.loads(callApi(url, payload, tokenKey))

    Dic={}
    for phrase in result:
        Value=phrase['word']
        Key=phrase['tags']['NER']['item1']
        if Key not in Dic:
            Dic[Key]=[]
        Dic[Key].append(Value)
    return (Dic)  

def NLP_Synonym(Word):
    baseUrl = "http://api.text-mining.ir/api/"
    url = baseUrl + "Token/GetToken"
    querystring = {"apikey":random.choice(Keys)}
    response = requests.request("GET", url, params=querystring)
    data = json.loads(response.text)
    tokenKey = data['token']

    url =  baseUrl + "TextSimilarity/ExtractSynonyms"
    payload = u'"'+Word+'"'
    return (callApi(url, payload, tokenKey))

def NLP_Similarity(Text,Text_):
    baseUrl = "http://api.text-mining.ir/api/"
    url = baseUrl + "Token/GetToken"
    querystring = {"apikey":random.choice(Keys)}
    response = requests.request("GET", url, params=querystring)
    data = json.loads(response.text)
    tokenKey = data['token']
    url =  baseUrl + "TextSimilarity/SentenceSimilarityBipartiteMatching"
    payload = u'{"string1":'+'"'+Text+'"'+',"string2":'+'"'+Text_+'"'+',"distanceFunc": 2}'  # JaccardDistance
    return (callApi(url, payload, tokenKey))

def NLP_Sentiment(Text):    #0:Neg  1:None   2:Pos
    baseUrl = "http://api.text-mining.ir/api/"
    url = baseUrl + "Token/GetToken"
    querystring = {"apikey":random.choice(Keys)}
    response = requests.request("GET", url, params=querystring)
    data = json.loads(response.text)
    tokenKey = data['token']
    
    url =  baseUrl + "SentimentAnalyzer/SentimentClassifier"
    payload = u'"'+Text+'"'
    return (callApi(url, payload, tokenKey))

import time
a=input()
s=time.time()
print (NLP_Ner(a))
print (time.time()-s)