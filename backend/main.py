from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .app.database import SessionLocal, engine
from .app.models import Base, User
from .app.schemas import UserCreate
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Medical API Running"}


@app.post("/users")

def create_user(user: UserCreate, db: Session = Depends(get_db)):

    new_user = User(
        name=user.name,
        email=user.email,
        phone=user.phone,
        address=user.address,
        medical_problem=user.medical_problem
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user