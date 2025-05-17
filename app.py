import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("🌍 Travel Recommendation System")

@st.cache_data
def load_data():
    return pd.read_csv("data/Travel Dataset.csv")

data = load_data()

# ✅ Create 'tags' column using available fields
required_columns = ['Name', 'State', 'Zone', 'Type', 'Significance']

if all(col in data.columns for col in required_columns):
    data['tags'] = (
        data['Name'].fillna('') + ' ' +
        data['State'].fillna('') + ' ' +
        data['Zone'].fillna('') + ' ' +
        data['Type'].fillna('') + ' ' +
        data['Significance'].fillna('')
    )

    cv = CountVectorizer(max_features=5000, stop_words='english')
    vector = cv.fit_transform(data['tags']).toarray()
    similarity = cosine_similarity(vector)

    def recommend(name):
        name = name.lower()
        if name not in data['Name'].str.lower().values:
            return ["❌ Place not found in dataset."]
        index = data[data['Name'].str.lower() == name].index[0]
        distances = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)
        recommendations = [data.iloc[i[0]].Name for i in distances[1:6]]
        return recommendations

    user_input = st.text_input("✈️ Enter the name of a tourist place you like:")

    if st.button("Recommend"):
        if user_input.strip() == "":
            st.warning("Please enter a valid place name.")
        else:
            results = recommend(user_input)
            st.write("Here are some places you might like:")
            for r in results:
                st.write("✅", r)

else:
    st.error("❌ Dataset is missing required columns: " + ", ".join(required_columns))
