# Travel-Recommendation-System
AI-Powered Travel Destination Recommender


A content-based Travel Recommendation System that helps users discover similar tourist destinations based on a place they already like. Built using Streamlit and deployed on Streamlit Cloud.

---

## Overview

This project uses a content-based filtering approach to recommend tourist attractions within India. Users can input the name of a place they like, and the system will suggest other similar places by analyzing features like zone, state, type, and significance of destinations.

The app is designed with simplicity in mind and is deployed using Streamlit Cloud for easy access and interaction.

---

## Features

- Place-Based Search – Users can enter a place they like and get similar recommendations.
- Content-Based Filtering – Uses available features like `Name`, `State`, `Zone`, `Type`, and `Significance`.
- Deployed on Streamlit Cloud – Accessible from anywhere, no local setup required.
- Fast & Lightweight – Built on efficient text vectorization and similarity computation.

---

## Algorithm & Techniques Used

- Natural Language Processing:
  - Combined multiple fields (`Name`, `State`, `Zone`, `Type`, `Significance`) to create a rich `tags` column for vectorization.
- CountVectorizer:
  - Converts text data into numerical vectors for similarity comparison.
- Cosine Similarity:
  - Measures the similarity between destinations based on text vector space.
- Streamlit:
  - For building and deploying the interactive web interface.

---

## Model Performance

Since this is a content-based recommendation system and not a supervised machine learning model, traditional metrics like accuracy, precision, and recall do not apply.

However, the system performs well in generating meaningful suggestions based on place features. Example:

**Input:** "Taj Mahal"  
**Output:** "Qutub Minar", "Gateway of India", "Red Fort", etc. — all similar historical monuments.

---

## How to Run the App

### Streamlit Cloud

[Launch the App](https://travel-recommendation-system-btx8rpnrs4pmvjgf7vbqm5.streamlit.app/) 

### Run Locally

```bash
git clone https://github.com/NethangiDissanayake/Travel-Recommendation-System.git
cd Travel-Recommendation-System
pip install -r requirements.txt
streamlit run app.py

