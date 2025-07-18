import requests

def emotion_detector(text_to_analyze): 
    # Sentiment Analysis Service URL
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # API header dictionary
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Text dictionary
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Send POST request to API
    response = requests.post(url, json = myobj, headers=header)
    return response.text
