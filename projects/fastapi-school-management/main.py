from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session

app = FastAPI()

# Database setup
DATABASE_URL = "sqlite:///./subjects.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLAlchemy Base
Base = declarative_base()

# Database Models
class Subject(Base):
    __tablename__ = "subjects"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    duration = Column(String)
    department = Column(String)

class TeachingFaculty(Base):
    __tablename__ = "teaching_faculty"
    
    id = Column(Integer, primary_key=True, index=True)
    course = Column(String, index=True)
    faculty = Column(String)

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models for API responses
class SubjectResponse(BaseModel):
    id: int
    name: str
    duration: str
    department: str

class SubjectFacultyResponse(BaseModel):
    subject: SubjectResponse
    faculty: str

async def list_of_subject_faculty_teaching(db: Session):
    subjects = db.query(Subject).all()
    result = []
    
    for subject in subjects:
        # Find the faculty for this subject
        faculty_record = db.query(TeachingFaculty).filter(TeachingFaculty.course == subject.name).first()
        faculty = faculty_record.faculty if faculty_record else None
        
        result.append({
            "subject": {
                "id": subject.id,
                "name": subject.name,
                "duration": subject.duration,
                "department": subject.department
            },
            "faculty": faculty
        })
    
    return result

@app.get("/subjects-faculty", response_model=list[SubjectFacultyResponse])
async def get_subjects_faculty(db: Session = Depends(get_db)):
    return await list_of_subject_faculty_teaching(db)
