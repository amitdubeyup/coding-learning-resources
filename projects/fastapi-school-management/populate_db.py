#!/usr/bin/env python3

from sqlalchemy.orm import sessionmaker
from main import Subject, TeachingFaculty, engine, Base

# Create tables
Base.metadata.create_all(bind=engine)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

# Data from schema.py
subjects = [
    {"id": 1, "name": "Mathematics", "duration": "6 months", "department": "Science"},
    {"id": 2, "name": "Physics", "duration": "6 months", "department": "Science"},
    {"id": 3, "name": "Chemistry", "duration": "6 months", "department": "Science"},
]

teaching_faculty = [
    {"course": "Mathematics", "faculty": "Dr. Smith"},
    {"course": "Physics", "faculty": "Dr. Johnson"},
    {"course": "Chemistry", "faculty": "Dr. Lee"},
]

try:
    # Clear existing data
    db.query(Subject).delete()
    db.query(TeachingFaculty).delete()
    
    # Insert subjects
    for subject_data in subjects:
        subject = Subject(
            id=subject_data["id"],
            name=subject_data["name"],
            duration=subject_data["duration"],
            department=subject_data["department"]
        )
        db.add(subject)
    
    # Insert teaching faculty
    for faculty_data in teaching_faculty:
        faculty = TeachingFaculty(
            course=faculty_data["course"],
            faculty=faculty_data["faculty"]
        )
        db.add(faculty)
    
    # Commit changes
    db.commit()
    print("Database populated successfully!")
    
    # Verify data
    subjects_count = db.query(Subject).count()
    faculty_count = db.query(TeachingFaculty).count()
    print(f"Added {subjects_count} subjects and {faculty_count} faculty records")
    
except Exception as e:
    print(f"Error populating database: {e}")
    db.rollback()
finally:
    db.close()