# Movie Recommendation App

A full-stack web application that allows users to register, log in, and receive movie recommendations based on their favorite genre.

## Tech Stack

- **Backend:** FastAPI, SQLAlchemy, SQLite
- **Frontend:** Streamlit
- **Other Tools:** Pydantic, Uvicorn, Requests

## Project Structure

```
movie_recommendation/
├── app.py                  # Streamlit frontend (in progress)
├── main.py                 # FastAPI entry point
├── database.py             # Database connection and session management
├── models/
│   └── movie_model.py      # User and Movie SQLAlchemy models
├── schemas/
│   ├── user_schema.py      # Pydantic schemas for User
│   └── movie_schema.py     # Pydantic schemas for Movie
├── services/
│   ├── user_services.py    # Business logic for user handling
│   └── movie_services.py   # Business logic for movies
├── controllers/
│   ├── user_controller.py  # API routes for users
│   └── movie_controller.py # API routes for movies
```

## Features

-  **User Registration** with `username`, `email`, `password`, and `favorite genre`
-  **User Login** with credential verification
-  **Personalized Recommendations** based on user's favorite genre
-  **FastAPI** backend with real-time JSON responses
-  **Streamlit UI** (in progress): registration, login, and movie display

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourname/movie_recommendation.git
cd movie_recommendation
````
### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Backend Server

```bash
uvicorn main:app --reload --port 8010
```

The API will be available at: [http://127.0.0.1:8010](http://127.0.0.1:8010)

### 4. Run the Streamlit Frontend

```bash
streamlit run app.py
```

##  API Endpoints

### User Endpoints

| Method | Endpoint              | Description                  |
|--------|-----------------------|------------------------------|
| POST   | `/users/register`     | Register a new user          |
| POST   | `/users/login`        | Login with credentials       |
| GET    | `/users/{username}`   | Get user details by username |
| GET    |"/users/{username}     | Get movies based on users    |
|        |  /recommendations"    | favourite genre              |

### Movie Endpoints

| Method | Endpoint                    | Description                       |
|--------|-----------------------------|-----------------------------------|
| GET    | `/movies/genre/{genre}`     | Get movies filtered by genre      |
|POST    |"/movies"                    |Post movie details                 |
|DELETE  |"/movies/{movie_id}"         |Delete movie details from the db   |
|PUT     |"/movies/{movie_id}"         |update the movie details           |
|GET     |""/movies""                  |Get all the movie details          |
|GET     |"/movies/{movie_id}"         |Get movie by the movie id          |

##  Example Request

### Register User

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepass",
  "liked_genre": "Action"
}
```

### Login User

{
  "username": "john_doe",
  "password": "securepass"
}
```

##  Known Issues

-  Backend is functional and returning expected results.
-  Streamlit UI is **in progress**:
  - UI loads and accepts input
  - Registration and login work
  - **Movie recommendations not yet displaying due to genre-fetching bug** (being debugged)

##  To Do

- [x] Build and test FastAPI backend
- [x] Implement user and movie models
- [x] Add login & registration with genre preferences
- [ ] Fix movie fetching logic in Streamlit
- [ ] Improve error handling and loading states
- [ ] Add styling and better UX to Streamlit

