import streamlit as st
import random

st.markdown("""
<style>



[data-testid="stAppViewContainer"] {
    background-image: url("https://plus.unsplash.com/premium_vector-1683120806506-d4299a64de7c?q=80&w=916&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* Dark Overlay */
[data-testid="stAppViewContainer"]::before{
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0,0,0,0.55);
    z-index: 0;
}

/* Main Content */
.main {
    position: relative;
    z-index: 1;
}

/* Title */
.title{
    text-align:center;
    color:white;
    font-size:50px;
    font-weight:bold;
    text-shadow: 2px 2px 10px black;
    margin-bottom:20px;
}

/* Glassmorphism Card */
.card{
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(15px);
    padding:30px;
    border-radius:20px;
    border:1px solid rgba(255,255,255,0.3);
    box-shadow:0px 8px 32px rgba(0,0,0,0.4);
}

/* Text */
.card h3,
.card p,
.card label{
    color:white !important;
}

/* Buttons */
.stButton > button{
    width:100%;
    height:50px;
    border-radius:12px;
    font-size:18px;
    font-weight:bold;
    border:none;
}

/* Attempts */
.attempts{
    text-align:center;
    color:#FFD700;
    font-size:22px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)
# Page Configuration
st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎯",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #667eea, #764ba2);
}

.title {
    text-align: center;
    color: white;
    font-size: 45px;
    font-weight: bold;
    margin-bottom: 20px;
}

.card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
}

.attempts {
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    color: #764ba2;
}

.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
}

.stNumberInput label {
    font-size: 18px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Initialize game state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0

# Title
st.markdown(
    '<div class="title">🎯 Number Guessing Game 🎮</div>',
    unsafe_allow_html=True
)

# Card Container
st.markdown('<div class="card">', unsafe_allow_html=True)

st.write("❓Guess a number between 1 and 100")

guess = int(st.number_input(
    "🔢Enter your guess:",
    min_value=1,
    max_value=100,
    step=1
))

if st.button("🎲 Guess"):
    st.session_state.attempts += 1

    if guess < st.session_state.number:
        st.warning("📉 Too Low! Try Again.")
    elif guess > st.session_state.number:
        st.warning("📈 Too High! Try Again.")
    else:
        st.balloons()
        st.success(
            f"🎉 Congratulations! You guessed the number in {st.session_state.attempts} attempts."
        )

if st.button("🔄 New Game"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.success("New Game Started!")

st.markdown(
    f'<p class="attempts">Attempts: {st.session_state.attempts}</p>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)
