import streamlit as st
import requests

st.title("News Summarization & Sentiment Analysis")

company = st.text_input("Enter Company Name")

if st.button("Fetch News"):
    if company:
        response = requests.get(f"http://127.0.0.1:5000/news?company={company}")

        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", [])
            
            for article in articles:
                st.subheader(article["title"])
                st.write("Summary:", article["summary"])
                st.write("Sentiment:", article["sentiment"])

            # Display Hindi audio file for HEADLINES
            if "audio_url" in data and data["audio_url"]:
                st.audio(data["audio_url"], format="audio/mp3")
            else:
                st.warning("No audio available.")

        else:
            st.error("Failed to fetch data. Try again!")




