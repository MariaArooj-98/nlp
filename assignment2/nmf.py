import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import matplotlib.pyplot as plt

# Sample text data with associated sentiments
corpus = [
    "I love this product. It's amazing!",
    "This movie is terrible. I hated it.",
    "The weather today is just okay.",
    "The food at that restaurant was excellent.",
    "I'm feeling neutral about this book."
]

sentiments = ['positive', 'negative', 'neutral', 'positive', 'neutral']

# Create a TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer(max_features=1000)
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)

# Apply NMF for topic extraction (2 topics as an example)
num_topics = 2
nmf = NMF(n_components=num_topics, random_state=1)
nmf_matrix = nmf.fit_transform(tfidf_matrix)

# Visualize the topics
for topic_idx, topic in enumerate(nmf.components_):
    top_words_idx = topic.argsort()[-10:][::-1]  # Top 10 words for each topic
    top_words = [tfidf_vectorizer.get_feature_names()[i] for i in top_words_idx]
    print(f"Topic {topic_idx + 1}: {', '.join(top_words)}")

# Plot sentiment distribution for each document
sentiment_counts = {s: 0 for s in set(sentiments)}
for sentiment in sentiments:
    sentiment_counts[sentiment] += 1

plt.bar(sentiment_counts.keys(), sentiment_counts.values())
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.title("Sentiment Distribution")
plt.show()
