import streamlit as st
import random

st.title("🎯 Number Guessing Game")

# Initialize game state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0

st.write("Guess a number between 1 and 100")

guess = st.number_input(
    "Enter your guess:",
    min_value=1,
    max_value=100,
    step=1
)

if st.button("Guess"):
    st.session_state.attempts += 1

    if guess < st.session_state.number:
        st.warning("📉 Too low! Try again.")
    elif guess > st.session_state.number:
        st.warning("📈 Too high! Try again.")
    else:
        st.success(
            f"🎉 Congratulations! You guessed the number in {st.session_state.attempts} attempts."
        )

if st.button("New Game"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.success("🔄 New game started!")

st.write(f"Attempts: {st.session_state.attempts}")