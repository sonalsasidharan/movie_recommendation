from pydantic import BaseModel
class MovieCreate(BaseModel):
    title: str
    genre: str

class MovieOut(BaseModel):
    id: int
    title: str
    genre: str

    class Config:
        orm_mode = True