from pydantic import BaseModel

class UserCreate(BaseModel):

    name: str
    email: str
    phone: str
    address: str
    medical_problem: str