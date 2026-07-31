# FastAPI User CRUD App

A simple FastAPI application with user management (CRUD) using PostgreSQL, SQLAlchemy, and Pydantic.

## Features
- User registration, listing, update, and deletion
- PostgreSQL database with SQLAlchemy ORM
- Password hashing with passlib
- Environment variable configuration

## Project Structure
```
fastapi/
  app/
    api/
      __init__.py
      user.py
    core/
      __init__.py
    crud/
      __init__.py
      user.py
    db/
      __init__.py
      session.py
    main.py
    models/
      __init__.py
      user.py
    schemas/
      __init__.py
      user.py
    utils/
      __init__.py
  README.md
  requirements.txt
  venv/
```

## Setup & Run
1. **Clone the repository**
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up PostgreSQL and .env file:**
   - Create a PostgreSQL database and user.
   - Create a `.env` file in the root directory and set your `DATABASE_URL` (see example below).
     
     Example `.env`:
     ```env
     DATABASE_URL=postgresql://username:password@localhost:5432/dbname
     ```
5. **Run migrations (if using Alembic) or create tables manually:**
   - (Manual method in Python shell):
   ```python
   from app.db.session import Base, engine
   from app.models.user import User
   Base.metadata.create_all(bind=engine)
   ```
6. **Start the app:**
   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints
- `POST /users/` - Create user
- `GET /users/` - List users
- `GET /users/{user_id}` - Get user by ID
- `PUT /users/{user_id}` - Update user
- `DELETE /users/{user_id}` - Delete user

## Notes
- Passwords are hashed using bcrypt.
- Update the `.env` file with your actual database credentials.
- The `venv/` directory is for your virtual environment and should not be committed to version control. 