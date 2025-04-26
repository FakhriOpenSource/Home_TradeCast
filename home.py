import streamlit as st
import time

# Set layout
st.set_page_config(page_title="TradeCast", layout="wide")

# Load custom CSS
def load_css():
    try:
        with open("home.css", "r") as f:
            css = f.read()
            st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("File CSS tidak ditemukan.")

load_css()

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("assets/bull_tradecast.png", width=300)


# Background overlay & konten utama
st.markdown("""
<div class="hero">
    <div class="overlay">
        <div class="container">
            <h1><br>Trade Smarter, Invest Better Powered by <span class="highlight">TradeCast</span></h1>
            <p class="typewriter">
              <span class="text-carousel"></span>
            </p>
            <a href="https://tradecast10-h99krzyzqbtgdtn8efx4pi.streamlit.app/" class="btn">Get started</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)




