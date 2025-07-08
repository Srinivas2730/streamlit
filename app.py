import streamlit as st
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample sentences
sentences = [
    "I love programming in Python",
    "Python is a great programming language",
    "I enjoy cooking Italian food",
    "Pasta is my favorite Italian dish",
    "Machine learning is fascinating",
    "My favorite fruit is orange",
    "Carrot is vegetable",
]

# Generate embeddings
embeddings = model.encode(sentences)

def get_closest_match(sentence, embeddings):
    query_embedding = model.encode([sentence])[0].reshape(1, -1)
    similarities = cosine_similarity(query_embedding, embeddings)[0]
    return sentences[np.argmax(similarities)]

st.title("Semantic Search Engine 🔍")
query = st.text_input("Enter a sentence:")

if query:
    match = get_closest_match(query, embeddings)
    st.success(f"Closest Match: {match}")