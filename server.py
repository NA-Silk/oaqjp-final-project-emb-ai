"""Main server file"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """Render index.html template"""
    return render_template('index.html')

@app.route("/emotionDetector")
def em_detector():
    """Run emotion_detector.py
    Return: a formatted string
    """
    # Retrieve text_to_analyze
    text_to_analyze = request.args.get('textToAnalyze')

    # Compute emotion_scores
    emotion_scores = emotion_detector(text_to_analyze)

    # Error handling
    if emotion_scores['dominant_emotion']:
        # Return formatted string
        output = f"""For the given statement, the system response is
         'anger': {emotion_scores['anger']},
         'disgust': {emotion_scores['disgust']},
         'fear': {emotion_scores['fear']},
         'joy': {emotion_scores['joy']},
         'sadness': {emotion_scores['sadness']}.
         The dominant emotion is {emotion_scores['dominant_emotion']}.
        """

    else:
        output = "Invalid text! Please try again!"

    return output

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
