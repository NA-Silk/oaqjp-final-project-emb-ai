import requests, json

def emotion_detector(text_to_analyze): 
    # Sentiment Analysis Service URL
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # API header dictionary
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Text dictionary
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Send POST request to API
    response = requests.post(url, json = myobj, headers=header)
    # Format response
    formatted_response = json.loads(response.text)

    # Collect emotion scores
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
    # Find dominant emotion

    d = list(emotion_scores.items()) # Convert to list of tuples
    d.sort(key=lambda x: x[1], reverse=True) # Sort by second element
    emotion_scores['dominant_emotion'] = d[0][0] # Add 'dominant_emotion' to dict

    return emotion_scores
