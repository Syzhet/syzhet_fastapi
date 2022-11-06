from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenCreate(BaseModel):
    username: str
    password: str
