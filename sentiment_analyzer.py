from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        sentiment = "Positive 😊"
    elif polarity < -0.1:
        sentiment = "Negative 😠"
    else:
        sentiment = "Neutral 😐"

    confidence = round(abs(polarity) * 100, 2)
    return sentiment, polarity, confidence


def main():
    print("🧠 AI Text Sentiment Analyzer")
    print("-" * 30)

    text = input("Enter a sentence to analyze: ")
    sentiment, polarity, confidence = analyze_sentiment(text)

    print("\n📊 Analysis Result")
    print(f"Sentiment   : {sentiment}")
    print(f"Polarity    : {polarity}")
    print(f"Confidence  : {confidence}%")


if __name__ == "__main__":
    main()
