from pydantic import BaseModel, ConfigDict


class Article(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    date_creation: str
    title: str
    markdown: str
    thumbnail: str
    color: str
