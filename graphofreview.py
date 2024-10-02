import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Load the combined master CSV file
master_csv_filename = "master_csv.csv"
df = pd.read_csv(master_csv_filename)

# Ensure the necessary columns exist (assuming 'Review' contains reviews and 'Company' contains company names)
if 'Review' not in df.columns or 'Company name' not in df.columns:
    raise ValueError("The dataset must contain 'Review' and 'Company' columns.")

# Initialize VADER sentiment intensity analyzer
sid = SentimentIntensityAnalyzer()

# Function to classify sentiment as 'Normal', 'Neutral', or 'Bad'
def classify_sentiment(review):
    if pd.isna(review):  # Handle NaN reviews
        return "Neutral"
    
    sentiment_score = sid.polarity_scores(review)
    compound = sentiment_score['compound']
    
    if compound >= 0.05:
        return 'Normal'  # Positive sentiment
    elif compound > -0.05 and compound < 0.05:
        return 'Neutral'  # Neutral sentiment
    else:
        return 'Bad'  # Negative sentiment

# Apply the sentiment classification to the 'Review' column
df['Sentiment'] = df['Review'].apply(classify_sentiment)

# Group by company and sentiment, then count the occurrences of each sentiment per company
company_sentiment_counts = df.groupby(['Company name', 'Sentiment']).size().unstack(fill_value=0)

# Plot the sentiment distribution for each company
company_sentiment_counts.plot(kind='bar', stacked=True, figsize=(10, 7), color=['green', 'gray', 'red'])

plt.xlabel('Company')
plt.ylabel('Number of Reviews')
plt.title('Sentiment Distribution of Reviews by Company')
plt.tight_layout()  # Adjust layout to make room for labels
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Display the graph
plt.show()
