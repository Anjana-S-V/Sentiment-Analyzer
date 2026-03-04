

* * * * *

AI Text Sentiment Analyzer
==========================

A simple Python-based AI project that analyzes the sentiment of user-input text and classifies it as **Positive**, **Negative**, or **Neutral** using Natural Language Processing (NLP).

This project demonstrates how pre-trained NLP tools can be used to build real-world AI applications without training complex machine learning models from scratch.

* * * * *

 Project Overview
-------------------

Sentiment analysis is widely used in:

-   Social media monitoring

-   Customer feedback analysis

-   Product review evaluation

-   Chatbot response systems

This project uses a pre-trained NLP library to:

1.  Accept user text input

2.  Analyze linguistic sentiment

3.  Calculate polarity score

4.  Classify emotional tone

5.  Display results clearly

It serves as a beginner-friendly introduction to applied AI and NLP.

* * * * *

 Features
-----------

-   Accepts user text input

-   Performs sentiment analysis using NLP

-   Classifies sentiment as:

    -   Positive

    -   Negative

    -   Neutral

-   Displays:

    -   Sentiment label

    -   Polarity score

    -   Confidence percentage

-   Clean and modular Python implementation

* * * * *

 How It Works
---------------

The system uses **TextBlob**, which is built on top of:

-   NLTK

-   Pattern

TextBlob calculates:

-   **Polarity** → Ranges from -1 (very negative) to +1 (very positive)

-   **Subjectivity** → Ranges from 0 (objective) to 1 (subjective)

### Classification Logic

-   Polarity > 0 → Positive

-   Polarity < 0 → Negative

-   Polarity ≈ 0 → Neutral

The confidence score is derived from the magnitude of the polarity value.

* * * * *

 Workflow
-----------

```
User Text Input
        ↓
Text Preprocessing
        ↓
TextBlob Sentiment Analysis
        ↓
Polarity & Subjectivity Calculation
        ↓
Sentiment Classification
        ↓
Result Display

```

* * * * *

 Tech Stack
-------------

### Programming Language

-   Python 3.x

### NLP Library

#### TextBlob

-   Pre-trained sentiment analyzer

-   Provides polarity and subjectivity scores

-   Simple and lightweight for beginners

* * * * *

 Project Structure
--------------------

```
AI_Text_Sentiment_Analyzer/
│
├── sentiment_analyzer.py
├── requirements.txt
└── README.md

```

* * * * *

 Installation & Setup
-----------------------

###  Clone the Repository

```
git clone https://github.com/your-username/AI_Text_Sentiment_Analyzer.git
cd AI_Text_Sentiment_Analyzer

```

###  Install Dependencies

```
pip install -r requirements.txt

```

If required:

```
python -m textblob.download_corpora

```

* * * * *

 Usage
--------

Run the script:

```
python sentiment_analyzer.py

```

Enter text when prompted, and the system will display:

-   Sentiment label

-   Polarity score

-   Confidence percentage

* * * * *

 Example Output
-----------------

Input:

```
I absolutely love this product! It works perfectly.

```

Output:

```
Sentiment: Positive
Polarity: 0.75
Confidence: 75%

```

* * * * *

 Privacy & Cost
-----------------

-   Fully local execution

-   No cloud APIs

-   No external data storage

-   100% free and open-source

* * * * *

 Learning Outcomes
--------------------

Through this project:

-   Understood basic NLP concepts

-   Implemented sentiment analysis

-   Learned polarity and subjectivity scoring

-   Built a simple AI classification system

-   Gained experience using pre-trained NLP models

* * * * *

 Future Enhancements
----------------------

-   Web-based interface (Streamlit)

-   Batch text file analysis

-   Visualization of sentiment trends

-   Multi-language sentiment support

-   Integration with social media APIs

* * * * *

 Use Cases
------------

-   Product review analysis

-   Social media sentiment monitoring

-   Feedback classification

-   Beginner AI/NLP demonstrations

* * * * *

 Author
------------

Anjana S V

