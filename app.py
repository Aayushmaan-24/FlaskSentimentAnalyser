from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        user_text = request.form.get("user_text")
        blob = TextBlob(user_text)

        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        # Determine sentiment
        if polarity > 0:
            sentiment = "Positive 😊"
        elif polarity < 0:
            sentiment = "Negative 😞"
        else:
            sentiment = "Neutral 😐"

        result = {
            "text": user_text,
            "polarity": round(polarity, 3),
            "subjectivity": round(subjectivity, 3),
            "sentiment": sentiment
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
