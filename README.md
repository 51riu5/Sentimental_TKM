<img width="1280" alt="readme-banner" src="https://github.com/user-attachments/assets/35332e92-44cb-425b-9dff-27bcf1023c6c">

# Sentiment Analysis with a TWIST! 🎯

## Basic Details
### Team Name: Avial

### Team Members
- Team Lead: Rishit Menon - TKM College of Engineering, Kollam
- Member 2: Arathy S - TKM College of Engineering, Kollam
- Member 3: Anand Gopan G - TKM College of Engineering, Kollam

### Project Description
A sentiment analysis project that combines NLP with YouTube Data API to match user-entered text with a mood-resonating video. Using a fine-tuned sentiment model, the tool identifies the text's tone as Positive, Neutral, or Negative. It then fetches a YouTube video aligned with the sentiment, providing users with mood-fitting content, from calming sounds to uplifting tunes. This project demonstrates practical applications of machine learning, API integration, and real-time content personalization.

### The Problem (that doesn't exist)
Ever felt like your text's emotions just aren't getting the attention they deserve? Are your words crying out for a matching YouTube vibe that no one asked for? Tired of your sad text getting upbeat music, or your cheerful text getting deep-focus tunes? You’re not alone in a problem no one knew they had!

### The Solution (that nobody asked for)
Enter Sentiment & Mood Matcher! We’ve taken your emotional text and decided it deserves its very own mood-matching YouTube video. By combining sentiment analysis with an API call, we pair your random thoughts with a perfectly mismatched or surprisingly relevant video—whether it’s calming music for your rants or motivational tunes for your grocery list musings. Because every text deserves its vibe, even if no one ever asked for it!

## Technical Details
### Technologies/Components Used
### For Software:
Languages used: Python
Frameworks used: None specifically; core functionality relies on libraries and APIs.
Libraries used:
Torch and transformers: for NLP and sentiment analysis
googleapiclient.discovery: to interact with the YouTube Data API
Numpy: for handling sentiment score arrays and label assignments
Tools used:
YouTube Data API v3: to fetch mood-matching YouTube videos based on sentiment

### Implementation
For Software:
# Installation
pip install torch transformers google-api-python-client numpy

# Run
python sentiment_analysis.py

### Project Documentation
For Software:
This project leverages natural language processing (NLP) and the YouTube Data API to provide a fun and engaging way to analyze text sentiment and recommend mood-appropriate videos. Below are the details of how the project is structured and how it operates:

Overview
Purpose: To analyze user-input text for sentiment and provide a corresponding YouTube video that matches the detected emotional tone.
Sentiment Classes: The project categorizes sentiment into three classes:
Positive: Indicates a happy or uplifting tone.
Neutral: Represents a balanced or indifferent sentiment.
Negative: Reflects a sad or discouraging tone.

Workflow
User Input:
The user is prompted to enter a statement or text that reflects their current thoughts or feelings.
Sentiment Analysis:
The input text is processed using a pre-trained sentiment analysis model (Cardiff NLP's Twitter RoBERTa model).
The model outputs a sentiment classification (Positive, Neutral, or Negative) based on the analysis of the input.
YouTube Video Fetching:
Depending on the sentiment classification, a relevant video query is generated:
For Positive sentiment, it searches for uplifting music.
For Neutral sentiment, it looks for focus music.
For Negative sentiment, it retrieves calming music.
The YouTube Data API is called to search for a video that matches the query.

Output:
The project displays the detected sentiment and provides a clickable link to the recommended YouTube video, allowing users to easily access mood-fitting content.
Dependencies
Python Libraries:
  torch: For model inference.
  transformers: For accessing and utilizing the sentiment analysis model.
  google-api-python-client: To interact with the YouTube API.
  numpy: For numerical operations related to sentiment scores.

Future Enhancements
User Interface: Develop a graphical user interface (GUI) for improved user interaction.
Additional Sentiment Classes: Explore the use of more nuanced sentiment classes for better personalization.
Video Personalization: Implement user preferences for a more tailored video recommendation experience.
This documentation provides an overview of the project’s functionality and structure, making it easier for contributors and users to understand and extend the project further.

# Screenshots (Add at least 3)
![Screenshot1]Outcome: Happy
![image](https://github.com/user-attachments/assets/b34e6c0c-d7d3-42aa-b025-cabdeb83015f)
*User inputs that he is happy and the algorithm determines his mental state and responds with a youtube video matching his vibe :)*

![Screenshot2]Outcome: Sad
![image](https://github.com/user-attachments/assets/863bd164-23fe-4eb1-86c0-b06bf6d7a7a7)
*User inputs he is not well and the algorithm detects his off-mood and recommends a soul filling youtube-video.*

![Screenshot3]Youtube Video
![image](https://github.com/user-attachments/assets/7c3c9d20-a426-4742-a3b1-c4c2a7e2e43a)
*Youtube Video which plays calm music*

# Diagrams
![Workflow](Add your workflow/architecture diagram here)
+-------------------+
|      Start        |
+-------------------+
         |
         v
+-------------------+
|    Input Text     |
|   (User Input)    |
+-------------------+
         |
         v
+-------------------+
|   Tokenization    |
|   (Tokenize Text) |
+-------------------+
         |
         v
+-------------------+
|  Model Prediction |
|  (Pass to Model)  |
+-------------------+
         |
         v
+--------------------+
|    Get Scores      |
|  (Sentiment Scores)|
+--------------------+
         |
         v
+---------------------+
|  Determine Sentiment|
| (Negative, Neutral, |
|    Positive)        |
+---------------------+
         |
         v
+---------------------+
|   Select Video URL  |
| (Based on Sentiment)|
+---------------------+
         |
         v
+--------------------+
|   Return Results   |
| (Sentiment & Video)|
+--------------------+
         |
         v
+-------------------+
|        End        |
+-------------------+

### Project Demo
# Video
https://drive.google.com/drive/folders/1VMQ5ADpL-QWo-CVlr7MJ_eUyKyEl-eqw?usp=sharing
*Tutorial on how to I/O and types of YT Videos being shown.*

## Team Contributions
- Rishit: Developed the sentiment analysis logic, integrated the pre-trained model, and implemented the video selection algorithm.
- Arathy: Designed the project structure, wrote the initial code for user input handling, and ensured API communication works seamlessly.
- Anand: Created the documentation, worked on testing the application for edge cases, and contributed to the user interface design.

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProject--24-24?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)



