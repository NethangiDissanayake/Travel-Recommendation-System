import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("🌍 Travel Recommendation System")

@st.cache_data
def load_data():
    return pd.read_csv("travel_recommendation_data.csv")

data = load_data()

# 🔍 TEMP: Show column names to debug
st.write("Columns in the dataset:", data.columns.tolist())

# ✅ Only create 'tags' if required columns exist
required_columns = ['Place', 'Country', 'Type', 'Description']

if all(col in data.columns for col in required_columns):
    data['tags'] = (
        data['Place'].fillna('') + ' ' +
        data['Country'].fillna('') + ' ' +
        data['Type'].fillna('') + ' ' +
        data['Description'].fillna('')
    )

    # Proceed with recommendation system
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vector = cv.fit_transform(data['tags']).toarray()
    similarity = cosine_similarity(vector)

    def recommend(place):
        place = place.lower()
        if place not in data['Place'].str.lower().values:
            return ["❌ Place not found in dataset."]
        index = data[data['Place'].str.lower() == place].index[0]
        distances = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)
        recommendations = [data.iloc[i[0]].Place for i in distances[1:6]]
        return recommendations

    user_input = st.text_input("✈️ Enter a place you like:")

    if st.button("Recommend"):
        if user_input.strip() == "":
            st.warning("Please enter a valid place.")
        else:
            results = recommend(user_input)
            st.write("Here are some places you might like:")
            for r in results:
                st.write("✅", r)

else:
    st.error("❌ Dataset is missing required columns: " + ", ".join(required_columns))
