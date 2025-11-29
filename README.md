# Sentiment Analysis Web Application

A simple and elegant web application built with Flask that performs sentiment analysis on user-provided text. The application uses TextBlob's natural language processing capabilities to analyze text and determine its sentiment (positive, negative, or neutral), along with polarity and subjectivity scores.

## Features

- **Real-time Sentiment Analysis**: Analyze the sentiment of any text input instantly
- **Polarity Score**: Get a numerical polarity score ranging from -1 (negative) to +1 (positive)
- **Subjectivity Score**: Understand how subjective or objective the text is (0 = objective, 1 = subjective)
- **Modern UI**: Clean and responsive web interface with smooth animations
- **Easy to Use**: Simple text input form with clear results display

## Technologies Used

- **Flask**: Python web framework for building the application
- **TextBlob**: Python library for processing textual data and performing sentiment analysis
- **NLTK**: Natural Language Toolkit (dependency of TextBlob)
- **HTML/CSS**: Frontend with modern styling and animations

## Requirements

- Python 3.11+ (tested with Python 3.11.2)
- pip (Python package installer)

## Installation

1. **Clone the repository** (or navigate to the project directory):
   ```bash
   cd SentimentAnalysis
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Download NLTK data** (required for TextBlob):
   ```bash
   python -c "import nltk; nltk.download('punkt'); nltk.download('brown'); nltk.download('movie_reviews')"
   ```

## Usage

1. **Start the Flask application**:
   ```bash
   python app.py
   ```

2. **Open your web browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Enter text** in the text area and click "Analyze Sentiment"

4. **View the results**:
   - Sentiment classification (Positive 😊, Negative 😞, or Neutral 😐)
   - Polarity score (ranges from -1 to +1)
   - Subjectivity score (ranges from 0 to 1)

## Project Structure

```
SentimentAnalysis/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Frontend HTML template
├── venv/                 # Virtual environment (not included in git)
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## How It Works

1. The user submits text through the web form
2. Flask receives the POST request and extracts the text
3. TextBlob analyzes the text and calculates:
   - **Polarity**: Measures how positive or negative the text is
   - **Subjectivity**: Measures how opinionated or factual the text is
4. The sentiment is classified based on polarity:
   - `polarity > 0`: Positive
   - `polarity < 0`: Negative
   - `polarity = 0`: Neutral
5. Results are displayed to the user with color-coded sentiment labels

## Example

**Input Text:**
```
"I love this product! It's amazing and works perfectly."
```

**Output:**
- **Sentiment**: Positive 😊
- **Polarity**: 0.625
- **Subjectivity**: 0.6

## Development

The application runs in debug mode by default. To disable debug mode, modify `app.py`:

```python
if __name__ == "__main__":
    app.run(debug=False)
```

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements..

