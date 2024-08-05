Movie Recommender System
This Streamlit-based Movie Recommender System leverages machine learning to suggest movies based on user input. The system utilizes a content-based filtering approach with TF-IDF vectorization and cosine similarity for recommendation.

Key Features:
Movie Details Retrieval: Fetches and displays movie posters, release dates, genres, and overviews using The Movie Database (TMDb) API.
Recommendation Engine: Uses precomputed movie similarity data to generate recommendations. Similarity is calculated using cosine similarity on TF-IDF features extracted from movie descriptions.
Interactive UI: Provides a dropdown menu for selecting a movie and a button to generate recommendations. Results include movie posters and detailed information for each recommended title.
Libraries and Technologies:
Streamlit: For building the interactive web app.
Requests: For API calls to TMDb.
Pickle: For loading pre-trained similarity data and movie metadata.
Scikit-learn: For TF-IDF vectorization and similarity computation.
NLTK: For text preprocessing (lemmatization and stopword removal).
Usage:
Select a movie from the dropdown menu.
Click "Recommend" to fetch and display movie recommendations.
Ensure to have the required pickle files (movies.pkl and similarity.pkl) in the working directory for the system to function correctly.
