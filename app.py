import streamlit as st
import pandas as pd
import pickle

# Page config - MUST be first Streamlit command
st.set_page_config(
    page_title="🎬 CineMatch - Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Simplified and optimized CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    font-family: 'Poppins', sans-serif;
}

.main-header {
    text-align: center;
    padding: 2.5rem 2rem;
    background: rgba(255, 255, 255, 0.95);
    border-radius: 20px;
    margin: 1.5rem auto 2rem auto;
    max-width: 700px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.main-title {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #667eea, #764ba2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
}

.main-subtitle {
    font-size: 1.1rem;
    color: #555;
    margin: 0;
}

.selection-container {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 15px;
    padding: 2rem;
    margin: 1.5rem auto;
    max-width: 500px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}

.selection-title {
    font-size: 1.4rem;
    font-weight: 600;
    color: #333;
    text-align: center;
    margin-bottom: 1rem;
}

.stButton > button {
    background: linear-gradient(135deg, #ff6b6b, #ffa500);
    color: white;
    border: none;
    border-radius: 20px;
    padding: 0.8rem 2rem;
    font-size: 1.1rem;
    font-weight: 600;
    width: 100%;
}

.movie-card {
    background: white;
    border-radius: 15px;
    padding: 1rem;
    margin: 0.5rem;
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
    text-align: center;
}

.movie-card:hover {
    transform: translateY(-5px);
}

.movie-poster {
    border-radius: 10px;
    width: 90%;
    height: 475px;
    object-fit: cover;
    margin-bottom: 1rem;
}

.movie-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: #333;
    margin-bottom: 0.5rem;
    line-height: 1.3;
}

.movie-rating {
    background: linear-gradient(135deg, #ffeaa7, #fdcb6e);
    color: #333;
    padding: 0.4rem 0.8rem;
    border-radius: 15px;
    font-size: 0.9rem;
    font-weight: 600;
    display: inline-block;
}

.recommendations-header {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 15px;
    padding: 2rem;
    text-align: center;
    margin: 2rem auto 1.5rem auto;
    max-width: 700px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}

.recommendations-title {
    font-size: 2.2rem;
    font-weight: 700;
    color: #333;
    margin-bottom: 0.5rem;
}

.recommendations-subtitle {
    font-size: 1rem;
    color: #666;
    margin: 0;
}

.feedback-container {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 15px;
    padding: 2rem;
    text-align: center;
    margin: 2rem auto;
    max-width: 600px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display: none;}

</style>
""", unsafe_allow_html=True)

# Load data function - simplified
@st.cache_data
def load_data():
    try:
        movies_dict = pickle.load(open('movies_dict.pkl','rb'))
        movies = pd.DataFrame(movies_dict)
        similarity = pickle.load(open('similarity.pkl','rb'))
        return movies, similarity
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None

# Recommendation function - simplified
def recommend(movie, movies, similarity):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        
        recommended_movies = []
        recommended_movies_posters = []
        
        for i in movies_list:
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_movies_posters.append(movies.iloc[i[0]].Poster_URL)
            
        return recommended_movies, recommended_movies_posters
    except Exception as e:
        st.error(f"Error getting recommendations: {e}")
        return [], []

# Main function

def main():
    # Load data
    movies, similarity = load_data()
    
    if movies is None or similarity is None:
        st.error("Failed to load movie data. Please check your files.")
        return
    
    # Initialize session state FIRST
    if 'show_recommendations' not in st.session_state:
        st.session_state.show_recommendations = False
    if 'selected_movie' not in st.session_state:
        st.session_state.selected_movie = None
    if 'recommended_movies' not in st.session_state:
        st.session_state.recommended_movies = []
    if 'recommended_posters' not in st.session_state:
        st.session_state.recommended_posters = []
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1 class="main-title">🎬 CineMatch</h1>
        <p class="main-subtitle">Discover your next favorite movie with AI-powered recommendations</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Selection section
    st.markdown("""
    <div class="selection-container">
        <h2 class="selection-title" style="color: #555;">🎭 Choose a movie you love!</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Movie selection
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        selected_movie_name = st.selectbox(
            'Pick a movie:',
            movies['title'].values,
            index=0,
            label_visibility="collapsed"
        )
        
        if st.button('🔮 Get Recommendations'):
            # Store everything in session state
            st.session_state.show_recommendations = True
            st.session_state.selected_movie = selected_movie_name
            names, posters = recommend(selected_movie_name, movies, similarity)
            st.session_state.recommended_movies = names
            st.session_state.recommended_posters = posters
    
    # Show recommendations if they exist in session state
    if st.session_state.show_recommendations and st.session_state.recommended_movies:
        # Show recommendations header
        st.markdown(f"""
        <div class="recommendations-header">
            <h2 class="recommendations-title" style="color: #555;">✨ Your Recommendations</h2>
            <p class="recommendations-subtitle">Based on <strong>{st.session_state.selected_movie}</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Display movies
        cols = st.columns(5)
        
        for i, (name, poster) in enumerate(zip(st.session_state.recommended_movies, st.session_state.recommended_posters)):
            with cols[i]:
                st.markdown(f"""
                <div class="movie-card">
                    <img src="{poster}" class="movie-poster" alt="{name}" 
                         onerror="this.src='https://via.placeholder.com/300x450/cccccc/666666?text=No+Image'">
                    <div class="movie-title">{name}</div>
                    <div class="movie-rating">⭐ Recommended</div>
                </div>
                """, unsafe_allow_html=True)
        
        # Feedback section
        st.markdown("""
        <div class="feedback-container">
            <h3 style="color: #333; margin-bottom: 1rem;">💭 How did we do?</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Feedback buttons with immediate response
        fb_col1, fb_col2, fb_col3 = st.columns(3)
        
        with fb_col1:
            if st.button("👍 Great!", use_container_width=True, key="feedback_great"):
                st.balloons()
                st.success("🎉 Fantastic! We're thrilled you loved our recommendations! Happy watching!")
        
        with fb_col2:
            if st.button("👌 Good", use_container_width=True, key="feedback_good"):
                st.success("😊 Great to hear! We're always working to make our suggestions even better!")
        
        with fb_col3:
            if st.button("👎 Could be better", use_container_width=True, key="feedback_improve"):
                st.info("📝 Thanks for the honest feedback! We'll use this to improve our recommendation engine!")



if __name__ == "__main__":
    main()








