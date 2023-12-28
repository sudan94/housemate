from pydantic import BaseModel

class GroupBase(BaseModel):
    title: str
    description: str | None = None


class GroupCreate(GroupBase):
    pass

class Group(GroupBase):
    id: int

    class Config:
        orm_mode = True

class GroupUser(BaseModel):
    group_id: int

class GroupUserCreate(BaseModel):
    group_id: int
    user_id: int

    class Config:
        orm_mode = True

