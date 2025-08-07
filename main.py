from fastapi import FastAPI
from controllers.movie_controller import movie_router
from controllers.user_controller import user_router

app = FastAPI()

app.include_router(movie_router)
app.include_router(user_router)