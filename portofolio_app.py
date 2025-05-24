import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Your Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for header
st.markdown("""
<style>
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Header styling */
    .header-container {
        background-color: #FFFFFF;
        width: 1250px; /* Or use max-width and margin: auto for responsiveness */
        margin: auto; /* Centers the header container itself */
        padding: 1rem 2rem;
        display: flex;
        /* Updated: Distribute items with space-between initially */
        justify-content: space-between; 
        align-items: center;
        border-bottom: 1px solid #333;
        margin-bottom: 2rem;
    }
    
    .header-brand {
        font-size: 1.5rem;
        font-weight: bold;
        color: black;
        /* Added: Give brand a fixed width to push other elements */
        flex-basis: 200px; /* Adjust as needed */
        text-align: left;
    }
    
    .header-nav {
        display: flex;
        gap: 2rem;
        align-items: center;
        /* Added: Use flex-grow to allow nav to take available space */
        flex-grow: 1; 
        /* Added: Center content within the nav container */
        justify-content: center; 
    }
    
    .nav-link {
        color: #ccc;
        text-decoration: none;
        font-size: 1rem;
    }
    
    .nav-link:hover {
        color: black;
    }
    
    .header-button {
        background-color: #333;
        color: black;
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
        border: none;
        cursor: pointer;
        /* Added: Give button a fixed width to push other elements */
        flex-basis: 150px; /* Adjust as needed */
        text-align: right;
    }
</style>
""", unsafe_allow_html=True)

# Header HTML
def render_header():
    st.markdown("""
    <div class="header-container">
        <div class="header-brand">Hello Farhan</div>
        <div class="header-nav">
            <a href="#" class="nav-link">Home</a>
            <a href="#" class="nav-link">About</a>
            <a href="#" class="nav-link">Projects</a>
            <a href="#" class="nav-link">Contact</a>
        </div>
        <button class="header-button">Call to Action</button>
    </div>
    """, unsafe_allow_html=True) # Ensure the button is directly inside header-container

# Render the header
render_header()

# Your main content goes here
st.write("Your page content...")