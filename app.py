import streamlit as st
import requests

API_URL = "http://127.0.0.1:8010" 

st.title("Movie Recommendation App")

if "username" not in st.session_state:
    st.session_state.username = None

menu = st.sidebar.selectbox("Menu", ["Login", "Register", "Logout"])

if menu == "Register":
    st.subheader("Create Account")
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
    try:
        res = requests.post(f"{API_URL}/users/register", json=payload)
        if res.status_code == 200:
            st.success("Registered successfully! Please login.")
        else:
            try:
                error_detail = res.json().get("detail", "Unknown error")
            except Exception as e:
                error_detail = f"Raw response: {res.text}\nError parsing JSON: {str(e)}"
            st.error(f"{error_detail}")
    except Exception as e:
        st.error(f"Request failed: {str(e)}")

elif menu == "Login":
    st.subheader("Login")
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login"):
        payload = {
            "username": username,
            "password": password
        }
        res = requests.post(f"{API_URL}/users/login", json=payload)
        if res.status_code == 200:
            st.session_state.username = username
            st.success(f"🎉 Logged in as {username}")
        else:
            st.error(f"{res.json()['detail']}")

elif menu == "Logout":
    st.session_state.username = None
    st.success(" Logged out.")

if st.session_state.username:
    st.subheader("Recommended Movies")
    res = requests.get(f"{API_URL}/users/{st.session_state.username}")
    if res.status_code == 200:
        user = res.json()
        liked_genre = user['liked_genre']

        st.info(f"Showing recommendations for genre: **{liked_genre}**")

       
        movie_res = requests.get(f"{API_URL}/movies/by-genre/{liked_genre}")
        if movie_res.status_code == 200:
            movies = movie_res.json()
            if movies:
                for movie in movies:
                    st.write(f"- {movie['title']} ({movie['genre']})")
            else:
                st.warning("No movies found in this genre.")
        else:
            st.error("Failed to fetch movies.")