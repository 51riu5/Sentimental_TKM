import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from googleapiclient.discovery import build
import numpy as np

# Load sentiment model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")

# Set up YouTube API client
youtube = build("youtube", "v3", developerKey="AIzaSyAmnLcKO3SfevG1kwrbBPXznButLpDNaI8")

def analyze_sentiment(text):
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    labels = ["Negative", "Neutral", "Positive"]
    sentiment_label = labels[np.argmax(scores)]
    return sentiment_label

def fetch_youtube_video(sentiment):
    query = ""
    if sentiment == "Positive":
        query = "uplifting music"
    elif sentiment == "Negative":
        query = "calming music"
    else:
        query = "focus music"

    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        q=query,
        type="video"
    )
    response = request.execute()
    video_id = response['items'][0]['id']['videoId']
    return f"https://www.youtube.com/watch?v={video_id}"

user_input = input("Enter your text for sentiment analysis: ")
sentiment = analyze_sentiment(user_input)
video_link = fetch_youtube_video(sentiment)
print(f"'{user_input}' - Sentiment: {sentiment}")
print(f"Here’s a video to match your sentiment: {video_link}")
