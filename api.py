from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import scrape_news
from summarizer import summarize_text
from sentiment import analyze_sentiment
from tts import generate_tts

app = Flask(__name__)
CORS(app)

@app.route("/news", methods=["GET"])
def get_news():
    company = request.args.get("company", "").strip()
    
    if not company:
        return jsonify({"error": "No company provided"}), 400

    articles = scrape_news(company)
    if not articles:
        return jsonify({"error": "No articles found"}), 404

    results = []
    headlines = []  # Store headlines for TTS

    for article in articles:
        title = article.get("title", "No Title")
        content = article.get("content", "")

        if not content:
            continue  

        summary = summarize_text(content)
        sentiment = analyze_sentiment(content)
        headlines.append(title)  # Collect only headlines

        results.append({
            "title": title,
            "summary": summary,
            "sentiment": sentiment
        })

    if not results:
        return jsonify({"error": "No valid articles found"}), 404

    # Generate Hindi speech from HEADLINES only
    audio_file = generate_tts(headlines, filename="news_headlines.mp3")

    response = {
        "company": company,
        "articles": results,
        "audio_url": f"http://127.0.0.1:5000/static/news_headlines.mp3" if audio_file else None
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)




