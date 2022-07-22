from pydantic import BaseModel, Field

class Data(BaseModel):
    machine_id: str = Field(..., title="User Machine Id")

class Token(BaseModel):
    token: str = Field(..., title="User JWT")
