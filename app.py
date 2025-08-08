import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8010"

st.title("Movie Recommendation System")

menu = ["Register User", "Add Movie", "View Movies"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Register User":
    st.subheader("Register a New User")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    liked_genre = st.text_input("Favorite Genre")

    if st.button("Register"):
        payload = {
            "username": username,
            "email": email,
            "password": password,
            "liked_genre": liked_genre
        }
        response = requests.post(f"{BASE_URL}/users/register", json=payload)
        if response.status_code == 200:
            st.success("User registered successfully!")
        else:
            st.error(f"Error: {response.json().get('detail')}")

elif choice == "Add Movie":
    st.subheader("Add a New Movie")
    title = st.text_input("Movie Title")
    genre = st.text_input("Genre")

    if st.button("Add Movie"):
        payload = {"title": title, "genre": genre}
        response = requests.post(f"{BASE_URL}/movies/", json=payload)
        if response.status_code == 200:
            st.success("Movie added successfully!")
        else:
            st.error(f"Error: {response.json().get('detail')}")

elif choice == "View Movies":
    st.subheader("All Movies")
    response = requests.get(f"{BASE_URL}/movies/")
    if response.status_code == 200:
        movies = response.json()
        for movie in movies:
            st.write(f"🎥 {movie['title']} ({movie['genre']})")
    else:
        st.error("Could not fetch movies.")