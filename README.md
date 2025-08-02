# 🎬 Movie Recommender System - README

A sophisticated AI-powered movie recommendation system built with machine learning algorithms and deployed as an interactive Streamlit web application called **CineMatch**[1][2].

## 🔗 Live Demo

**🌐 Try it now:** https://movierecommendersystem-f9gaik45vgtfcwqpillpg8.streamlit.app/

## 📋 Overview

This project implements a content-based movie recommendation system that suggests similar movies based on user selection. The system analyzes movie features including genres, keywords, cast, crew, and plot overviews to find and recommend the most similar movies using advanced natural language processing and machine learning techniques[1][2].

## ✨ Features

- **Interactive Web Interface**: Clean, user-friendly Streamlit interface with movie selection dropdown[2]
- **AI-Powered Recommendations**: Get 5 personalized movie recommendations based on your selection[2]
- **Content-Based Filtering**: Uses movie metadata including genres, cast, crew, keywords, and plot summaries[1][2]
- **Real-time Processing**: Instant recommendations with movie poster integration[1]
- **User Feedback System**: Rate the recommendations to help improve the system[2]
- **Comprehensive Dataset**: Built on TMDB 5000 movie dataset with extensive movie information[1][2]

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Machine Learning**: scikit-learn
- **Data Processing**: pandas, numpy
- **Natural Language Processing**: NLTK (Porter Stemmer)
- **Similarity Computation**: Cosine Similarity
- **Data Source**: TMDB 5000 Movies Dataset
- **Deployment**: Streamlit Cloud

## 📊 Dataset

The system uses the comprehensive TMDB 5000 Movies Dataset containing:
- **Movies Dataset**: 4,803 movies with 20 features including budget, genres, homepage, keywords, original language, overview, popularity, production companies, release date, revenue, runtime, status, tagline, title, vote average, and vote count[1][2]
- **Credits Dataset**: 4,803 entries with 4 features including movie_id, title, cast, and crew information[1][2]

## 🧠 Machine Learning Pipeline

### 1. Data Preprocessing[1][2]
- **Data Merging**: Combines movies and credits datasets on movie_id
- **Feature Selection**: Extracts relevant features (movie_id, title, overview, genres, keywords, cast, crew)
- **Data Cleaning**: Handles missing values and removes duplicates
- **JSON Parsing**: Converts string representations of lists to actual lists using `ast.literal_eval()`

### 2. Feature Engineering[1][2]
- **Genre Extraction**: Parses nested JSON to extract genre names
- **Keywords Processing**: Extracts relevant keywords from metadata
- **Cast Information**: Retrieves top 3 cast members from each movie
- **Crew Processing**: Focuses specifically on director information
- **Text Normalization**: Removes spaces from multi-word names/terms to treat them as single entities

### 3. Text Processing[1][2]
- **Feature Combination**: Merges overview, genres, keywords, cast, and crew into unified 'tags'
- **Stemming**: Applies Porter Stemmer to reduce words to root forms (e.g., "action", "actions" → "action")
- **Vectorization**: Uses CountVectorizer with 5000 max features and English stop words removal
- **Bag of Words**: Creates numerical representation of text features

### 4. Similarity Computation[1][2]
- **Cosine Similarity**: Computes similarity matrix (4806 × 4806) between all movies
- **Recommendation Algorithm**: For each movie, finds top 5 most similar movies based on cosine similarity scores
- **Ranking**: Sorts movies by similarity scores in descending order

## 📁 Project Structure

```
Movie_Recommender_System/
├── app.py                                    # Main Streamlit application
├── FinalizedMovieRecomenderSystem.ipynb     # Jupyter notebook with ML pipeline
├── requirements.txt                          # Python dependencies
├── movies_dict.pkl                          # Processed movies data (pickle file)
├── similarity.pkl                           # Precomputed similarity matrix (pickle file)
├── FinalDF.csv                             # Final processed dataset
├── tmdb_5000_movies.csv                    # Original movies dataset
├── tmdb_5000_credits.csv                   # Original credits dataset
├── README.md                               # Project documentation
└── LICENSE                                 # MIT License
```

## 📈 Performance Metrics

- **Dataset Size**: 4,806 movies processed[1][2]
- **Feature Vector**: 5,000 dimensional sparse matrix[1][2]
- **Similarity Matrix**: 4,806 × 4,806 precomputed cosine similarities[1][2]
- **Response Time**: Near-instantaneous recommendations using precomputed similarities[1]
- **Accuracy**: Content-based filtering ensures thematically relevant recommendations[1][2]

## 📞 Contact

**Laaksh Parikh** - [@Laaksh1205](https://github.com/Laaksh1205)

**Project Link**: https://github.com/Laaksh1205/Movie_Recommender_System
