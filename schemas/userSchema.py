from pydantic import BaseModel



# this is the base class of user
class UserBase(BaseModel):
    email: str
    name: str
    is_active: bool

# this is to create a user with extend class userbase
class UserCreate(UserBase):
    pass

# this is to retrun the user
class User(UserBase):
    id: int

    class Config:
        orm_mode = True