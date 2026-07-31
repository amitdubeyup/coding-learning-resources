# FastAPI Interview Questions & Guide

## Table of Contents
1. [FastAPI Basics](#fastapi-basics)
2. [Async Programming](#async-programming)
3. [Pydantic Models & Validation](#pydantic-models--validation)
4. [Dependency Injection](#dependency-injection)
5. [API Architecture & Best Practices](#api-architecture--best-practices)
6. [Performance & Optimization](#performance--optimization)
7. [Testing](#testing)
8. [Production & Deployment](#production--deployment)
9. [Advanced Patterns](#advanced-patterns)

---

## FastAPI Basics

### Q1: What is FastAPI and why would you choose it over Flask or Django?
**Answer:**
FastAPI is a modern, high-performance web framework for building APIs with Python 3.7+ based on standard Python type hints. Key advantages:

**Advantages over Flask:**
- Built-in async/await support
- Automatic API documentation (OpenAPI/Swagger)
- Request/response validation using Pydantic
- Better performance (comparable to Node.js)
- Type hints for better IDE support

**Advantages over Django:**
- Lighter weight and faster
- Modern async-first design
- Better for microservices
- Less boilerplate code
- Native WebSocket support

**Example:**
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "price": item.price}
```

### Q2: How does FastAPI handle request validation automatically?
**Answer:**
FastAPI uses Pydantic models for automatic request validation. When you define a Pydantic model as a parameter type, FastAPI:
1. Reads the request body
2. Validates the data type and constraints
3. Converts the data to the model instance
4. Returns detailed error messages if validation fails

**Example:**
```python
from pydantic import BaseModel, Field, validator

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str
    age: int = Field(..., gt=0, lt=150)

    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email')
        return v

@app.post("/users/")
async def create_user(user: User):
    return user
```

### Q3: Explain the difference between path parameters, query parameters, and request body in FastAPI
**Answer:**

**Path Parameters:**
- Part of the URL path
- Required by default
- Defined in the route path

```python
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

**Query Parameters:**
- Come after `?` in URL
- Optional by default
- Can have default values

```python
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

**Request Body:**
- Sent in POST/PUT/PATCH requests
- Defined using Pydantic models
- Automatically validated

```python
@app.post("/items/")
async def create_item(item: Item):
    return item
```

---

## Async Programming

### Q4: Explain async/await in FastAPI and when to use it
**Answer:**
Async/await allows non-blocking I/O operations, enabling better concurrency and performance.

**When to use async:**
- Database queries
- External API calls
- File I/O operations
- Any I/O-bound operations

**When NOT to use async:**
- CPU-intensive computations
- Synchronous libraries that don't support async

**Example:**
```python
import httpx
from sqlalchemy.ext.asyncio import AsyncSession

@app.get("/external-data/")
async def get_external_data():
    # Good: Async HTTP client
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.example.com/data")
    return response.json()

@app.get("/users/{user_id}")
async def get_user(user_id: int, db: AsyncSession):
    # Good: Async database query
    result = await db.execute(select(User).filter(User.id == user_id))
    return result.scalar_one_or_none()

@app.get("/compute/")
async def compute():
    # Bad: CPU-intensive operation in async function
    result = sum(range(1000000))  # This blocks the event loop
    return {"result": result}
```

### Q5: How does FastAPI handle concurrent requests with asyncio?
**Answer:**
FastAPI runs on an ASGI server (like Uvicorn) that uses asyncio event loop. When a request comes in:

1. The event loop schedules the async handler
2. When the handler hits an `await`, it yields control
3. Other requests can be processed while waiting
4. When the awaited operation completes, the handler resumes

**Example:**
```python
import asyncio

@app.get("/slow")
async def slow_endpoint():
    # Simulates a slow database query
    await asyncio.sleep(5)
    return {"status": "done"}

# Multiple requests can run concurrently
# 10 requests take ~5 seconds total, not 50 seconds
```

### Q6: What's the difference between `def` and `async def` in FastAPI endpoints?
**Answer:**

**Using `async def`:**
- Runs in the main event loop
- Should use `await` for I/O operations
- Best for async operations

**Using `def`:**
- Runs in a thread pool
- Can use synchronous libraries
- FastAPI handles the async wrapping automatically

**Example:**
```python
# Async endpoint (preferred for async operations)
@app.get("/async-db")
async def async_db_query(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()

# Sync endpoint (for sync libraries)
@app.get("/sync-db")
def sync_db_query(db: Session):
    return db.query(User).all()
```

---

## Pydantic Models & Validation

### Q7: How do you use Pydantic for complex data validation?
**Answer:**
Pydantic provides powerful validation through field constraints, custom validators, and model configuration.

**Example:**
```python
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zipcode: str = Field(..., regex=r'^\d{5}$')

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str
    password: str = Field(..., min_length=8)
    age: Optional[int] = Field(None, ge=0, le=150)
    addresses: List[Address] = []
    created_at: datetime = Field(default_factory=datetime.now)

    @validator('email')
    def validate_email(cls, v):
        if '@' not in v or '.' not in v:
            raise ValueError('Invalid email format')
        return v.lower()

    @validator('password')
    def validate_password(cls, v):
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain a number')
        return v

    @root_validator
    def check_adult_with_address(cls, values):
        age = values.get('age')
        addresses = values.get('addresses')
        if age and age < 18 and addresses:
            raise ValueError('Minors cannot have addresses')
        return values

    class Config:
        validate_assignment = True
```

### Q8: Explain Pydantic's type hints and how FastAPI uses them
**Answer:**
Pydantic uses Python type hints for automatic validation, serialization, and documentation.

**Example:**
```python
from typing import List, Optional, Union, Dict
from pydantic import BaseModel, HttpUrl

class Product(BaseModel):
    name: str
    price: float
    tags: List[str] = []
    image_url: Optional[HttpUrl] = None
    metadata: Dict[str, Union[str, int, float]] = {}

@app.post("/products/")
async def create_product(product: Product):
    # FastAPI automatically:
    # 1. Validates all types
    # 2. Converts JSON to Product instance
    # 3. Generates OpenAPI documentation
    # 4. Returns validation errors if invalid
    return product
```

### Q9: How do you handle nested models and complex data structures?
**Answer:**
```python
from pydantic import BaseModel
from typing import List, Optional

class Author(BaseModel):
    name: str
    email: str

class Comment(BaseModel):
    text: str
    author: Author
    created_at: datetime

class Post(BaseModel):
    title: str
    content: str
    author: Author
    comments: List[Comment] = []
    tags: List[str] = []
    metadata: Optional[Dict[str, Any]] = None

@app.post("/posts/")
async def create_post(post: Post):
    # Automatically validates entire nested structure
    return post
```

---

## Dependency Injection

### Q10: What is dependency injection in FastAPI and why is it useful?
**Answer:**
Dependency injection is a system where dependencies (like database connections, authentication, etc.) are automatically provided to your endpoint functions.

**Benefits:**
- Code reusability
- Easy testing (can inject mock dependencies)
- Cleaner code separation
- Automatic validation and error handling

**Example:**
```python
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
) -> User:
    user = await authenticate_token(token, db)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid authentication")
    return user

@app.get("/me")
async def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user

@app.get("/items/")
async def read_items(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    items = await get_user_items(db, current_user.id, skip, limit)
    return items
```

### Q11: How do you implement authentication using dependencies?
**Answer:**
```python
from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

security = HTTPBearer()

async def verify_token(
    credentials: HTTPAuthorizationCredentials = Security(security)
) -> dict:
    try:
        payload = jwt.decode(
            credentials.credentials,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )

async def get_current_user(
    payload: dict = Depends(verify_token),
    db: AsyncSession = Depends(get_db)
) -> User:
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/protected")
async def protected_route(user: User = Depends(get_current_user)):
    return {"message": f"Hello {user.username}"}
```

### Q12: How do you handle dependency caching and optimization?
**Answer:**
```python
from functools import lru_cache
from fastapi import Depends

@lru_cache()
def get_settings():
    # This is cached, only loaded once
    return Settings()

# Sub-dependency pattern
async def common_parameters(
    skip: int = 0,
    limit: int = 100
):
    return {"skip": skip, "limit": limit}

async def db_with_pagination(
    commons: dict = Depends(common_parameters),
    db: AsyncSession = Depends(get_db)
):
    return {"db": db, **commons}

@app.get("/items/")
async def read_items(deps: dict = Depends(db_with_pagination)):
    # deps contains db, skip, and limit
    items = await get_items(deps["db"], deps["skip"], deps["limit"])
    return items
```

---

## API Architecture & Best Practices

### Q13: How do you structure a FastAPI application for scalability?
**Answer:**

**Project Structure:**
```
app/
├── main.py              # Application entry point
├── config.py            # Configuration settings
├── dependencies.py      # Global dependencies
├── models/              # SQLAlchemy models
│   ├── __init__.py
│   ├── user.py
│   └── item.py
├── schemas/             # Pydantic schemas
│   ├── __init__.py
│   ├── user.py
│   └── item.py
├── routers/             # API routes
│   ├── __init__.py
│   ├── users.py
│   └── items.py
├── services/            # Business logic
│   ├── __init__.py
│   ├── user_service.py
│   └── item_service.py
├── repositories/        # Database layer
│   ├── __init__.py
│   ├── user_repository.py
│   └── item_repository.py
├── middleware/          # Custom middleware
│   └── __init__.py
└── utils/               # Utility functions
    └── __init__.py
```

**Example Implementation:**
```python
# main.py
from fastapi import FastAPI
from app.routers import users, items

app = FastAPI(title="My API", version="1.0.0")

app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(items.router, prefix="/api/v1/items", tags=["items"])

# routers/users.py
from fastapi import APIRouter, Depends
from app.services.user_service import UserService

router = APIRouter()

@router.get("/")
async def get_users(
    service: UserService = Depends()
):
    return await service.get_all_users()
```

### Q14: How do you implement error handling and custom exceptions?
**Answer:**
```python
from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

# Custom exceptions
class ItemNotFoundError(Exception):
    def __init__(self, item_id: int):
        self.item_id = item_id

class InsufficientPermissionsError(Exception):
    pass

# Exception handlers
@app.exception_handler(ItemNotFoundError)
async def item_not_found_handler(request: Request, exc: ItemNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "detail": f"Item {exc.item_id} not found",
            "type": "item_not_found"
        }
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "detail": exc.errors(),
            "body": exc.body,
            "type": "validation_error"
        }
    )

# Using in endpoints
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    item = await get_item_from_db(item_id)
    if not item:
        raise ItemNotFoundError(item_id)
    return item
```

### Q15: How do you implement API versioning in FastAPI?
**Answer:**
```python
# Approach 1: URL Path Versioning
from fastapi import APIRouter

router_v1 = APIRouter(prefix="/api/v1")
router_v2 = APIRouter(prefix="/api/v2")

@router_v1.get("/users/")
async def get_users_v1():
    return {"version": "1.0", "users": []}

@router_v2.get("/users/")
async def get_users_v2():
    return {"version": "2.0", "users": [], "metadata": {}}

app.include_router(router_v1)
app.include_router(router_v2)

# Approach 2: Header-based Versioning
from fastapi import Header, HTTPException

async def verify_api_version(x_api_version: str = Header(default="1.0")):
    if x_api_version not in ["1.0", "2.0"]:
        raise HTTPException(status_code=400, detail="Invalid API version")
    return x_api_version

@app.get("/users/")
async def get_users(api_version: str = Depends(verify_api_version)):
    if api_version == "1.0":
        return {"users": []}
    else:
        return {"users": [], "metadata": {}}
```

---

## Performance & Optimization

### Q16: How do you optimize FastAPI applications for high performance?
**Answer:**

**1. Use Async Everywhere:**
```python
# Good
@app.get("/users/")
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    return result.scalars().all()

# Bad
@app.get("/users/")
def get_users_sync(db: Session = Depends(get_db)):
    return db.query(User).all()  # Blocks event loop
```

**2. Connection Pooling:**
```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

engine = create_async_engine(
    DATABASE_URL,
    pool_size=20,
    max_overflow=10,
    pool_pre_ping=True
)
```

**3. Response Caching:**
```python
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

@app.get("/expensive-operation/")
@cache(expire=60)  # Cache for 60 seconds
async def expensive_operation():
    # Expensive computation
    return {"result": "data"}
```

**4. Background Tasks:**
```python
from fastapi import BackgroundTasks

def send_email(email: str, message: str):
    # Slow email sending
    pass

@app.post("/send-notification/")
async def send_notification(
    email: str,
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(send_email, email, "Hello")
    return {"message": "Notification scheduled"}
```

**5. Streaming Responses:**
```python
from fastapi.responses import StreamingResponse
import asyncio

async def generate_data():
    for i in range(1000):
        yield f"data chunk {i}\n"
        await asyncio.sleep(0.01)

@app.get("/stream")
async def stream():
    return StreamingResponse(generate_data(), media_type="text/plain")
```

### Q17: How do you implement rate limiting and throttling?
**Answer:**
```python
from fastapi import Request, HTTPException
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/limited")
@limiter.limit("5/minute")
async def limited_route(request: Request):
    return {"message": "This endpoint is rate limited"}

# Custom rate limiter with Redis
import aioredis
from datetime import datetime, timedelta

async def rate_limit(
    request: Request,
    key: str,
    max_requests: int,
    window_seconds: int
):
    redis = request.app.state.redis
    current_time = datetime.now()
    window_start = current_time - timedelta(seconds=window_seconds)

    # Clean old requests
    await redis.zremrangebyscore(key, 0, window_start.timestamp())

    # Count requests in window
    request_count = await redis.zcard(key)

    if request_count >= max_requests:
        raise HTTPException(status_code=429, detail="Too many requests")

    # Add current request
    await redis.zadd(key, {str(current_time): current_time.timestamp()})
    await redis.expire(key, window_seconds)
```

### Q18: How do you handle large file uploads efficiently?
**Answer:**
```python
from fastapi import UploadFile, File
import aiofiles

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # Streaming upload for large files
    async with aiofiles.open(f"/tmp/{file.filename}", 'wb') as out_file:
        while content := await file.read(1024 * 1024):  # Read 1MB chunks
            await out_file.write(content)

    return {"filename": file.filename, "size": file.size}

# Multiple file uploads
@app.post("/upload-multiple/")
async def upload_multiple_files(files: List[UploadFile] = File(...)):
    results = []
    for file in files:
        async with aiofiles.open(f"/tmp/{file.filename}", 'wb') as out_file:
            await out_file.write(await file.read())
        results.append({"filename": file.filename})
    return results

# Chunked upload for very large files
@app.post("/upload-chunk/")
async def upload_chunk(
    chunk_number: int,
    total_chunks: int,
    file: UploadFile = File(...)
):
    filename = f"{file.filename}.part{chunk_number}"
    async with aiofiles.open(f"/tmp/{filename}", 'wb') as out_file:
        await out_file.write(await file.read())

    if chunk_number == total_chunks:
        # Combine all chunks
        await combine_chunks(file.filename, total_chunks)

    return {"chunk": chunk_number, "total": total_chunks}
```

---

## Testing

### Q19: How do you write unit tests for FastAPI endpoints?
**Answer:**
```python
from fastapi.testclient import TestClient
import pytest

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/users/",
        json={"username": "test", "email": "test@example.com"}
    )
    assert response.status_code == 200
    assert response.json()["username"] == "test"

def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert "username" in response.json()

def test_invalid_user():
    response = client.post(
        "/users/",
        json={"username": "a"}  # Too short
    )
    assert response.status_code == 422

# Async tests
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_async_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/users/")
    assert response.status_code == 200
```

### Q20: How do you test dependencies and authentication?
**Answer:**
```python
from fastapi import Depends

# Override dependencies for testing
async def override_get_db():
    # Return test database session
    yield test_db

async def override_get_current_user():
    return User(id=1, username="testuser")

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_protected_endpoint():
    response = client.get("/protected")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

# Clean up
app.dependency_overrides = {}
```

---

## Production & Deployment

### Q21: How do you deploy FastAPI to production?
**Answer:**

**Using Uvicorn with Gunicorn:**
```bash
gunicorn app.main:app \
    --workers 4 \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000 \
    --timeout 60 \
    --graceful-timeout 30
```

**Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "app.main:app", \
     "--workers", "4", \
     "--worker-class", "uvicorn.workers.UvicornWorker", \
     "--bind", "0.0.0.0:8000"]
```

**Docker Compose:**
```yaml
version: '3.8'
services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis

  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=mydb

  redis:
    image: redis:7
```

### Q22: How do you implement health checks and monitoring?
**Answer:**
```python
from fastapi import status
from datetime import datetime

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check(db: AsyncSession = Depends(get_db)):
    try:
        # Check database
        await db.execute("SELECT 1")

        # Check Redis
        await redis.ping()

        return {
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "checks": {
                "database": "ok",
                "redis": "ok"
            }
        }
    except Exception as e:
        return JSONResponse(
            status_code=503,
            content={
                "status": "unhealthy",
                "error": str(e)
            }
        )

# Prometheus metrics
from prometheus_client import Counter, Histogram, make_asgi_app

REQUEST_COUNT = Counter('request_count', 'Total requests')
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency')

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    REQUEST_COUNT.inc()
    with REQUEST_LATENCY.time():
        response = await call_next(request)
    return response

# Mount Prometheus metrics endpoint
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)
```

---

## Advanced Patterns

### Q23: How do you implement WebSocket connections in FastAPI?
**Answer:**
```python
from fastapi import WebSocket, WebSocketDisconnect
from typing import List

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Client {client_id}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client {client_id} left")
```

### Q24: How do you implement middleware for logging and request tracing?
**Answer:**
```python
import time
import uuid
from fastapi import Request
import logging

logger = logging.getLogger(__name__)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Generate request ID
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id

    # Log request
    logger.info(f"Request {request_id}: {request.method} {request.url}")

    # Measure request time
    start_time = time.time()

    # Process request
    response = await call_next(request)

    # Calculate duration
    duration = time.time() - start_time

    # Add headers
    response.headers["X-Request-ID"] = request_id
    response.headers["X-Process-Time"] = str(duration)

    # Log response
    logger.info(
        f"Request {request_id} completed in {duration:.3f}s "
        f"with status {response.status_code}"
    )

    return response
```

### Q25: How do you implement multi-tenancy in FastAPI?
**Answer:**
```python
from fastapi import Header, HTTPException, Depends

async def get_tenant_id(x_tenant_id: str = Header(...)) -> str:
    # Validate tenant
    if not await is_valid_tenant(x_tenant_id):
        raise HTTPException(status_code=400, detail="Invalid tenant")
    return x_tenant_id

async def get_tenant_db(
    tenant_id: str = Depends(get_tenant_id)
) -> AsyncSession:
    # Return tenant-specific database connection
    engine = get_tenant_engine(tenant_id)
    async with AsyncSession(engine) as session:
        yield session

@app.get("/items/")
async def get_items(
    tenant_id: str = Depends(get_tenant_id),
    db: AsyncSession = Depends(get_tenant_db)
):
    # Automatically filtered by tenant
    result = await db.execute(
        select(Item).filter(Item.tenant_id == tenant_id)
    )
    return result.scalars().all()

# Row-level security approach
@app.get("/items/")
async def get_items_rls(
    tenant_id: str = Depends(get_tenant_id),
    db: AsyncSession = Depends(get_db)
):
    # Set tenant context for row-level security
    await db.execute(f"SET app.current_tenant = '{tenant_id}'")
    result = await db.execute(select(Item))
    return result.scalars().all()
```

---

## Integration with React Frontend

### Q26: How do you handle CORS for React applications?
**Answer:**
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # React dev server
        "https://yourdomain.com"   # Production
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Development: Allow all origins (NOT for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Q27: How do you implement Server-Sent Events (SSE) for real-time updates?
**Answer:**
```python
from fastapi.responses import StreamingResponse
import asyncio

async def event_stream():
    while True:
        # Generate events
        yield f"data: {{'timestamp': '{datetime.now()}'}}\n\n"
        await asyncio.sleep(1)

@app.get("/events")
async def events():
    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream"
    )

# React client
"""
const eventSource = new EventSource('http://localhost:8000/events');
eventSource.onmessage = (event) => {
    console.log('New event:', JSON.parse(event.data));
};
"""
```

---

## Real-World Scenarios

### Q28: How would you implement a feature flag system?
**Answer:**
```python
from enum import Enum

class FeatureFlag(str, Enum):
    NEW_UI = "new_ui"
    BETA_FEATURES = "beta_features"
    AI_ASSISTANT = "ai_assistant"

async def check_feature_flag(
    feature: FeatureFlag,
    user: User = Depends(get_current_user)
) -> bool:
    # Check if feature is enabled for user
    flags = await get_user_feature_flags(user.id)
    return feature in flags

@app.get("/dashboard")
async def get_dashboard(
    user: User = Depends(get_current_user),
    new_ui: bool = Depends(lambda: check_feature_flag(FeatureFlag.NEW_UI))
):
    if new_ui:
        return {"version": "v2", "features": [...]}
    else:
        return {"version": "v1", "features": [...]}
```

### Q29: How do you implement data pagination efficiently?
**Answer:**
```python
from fastapi import Query
from typing import Generic, TypeVar, List
from pydantic import BaseModel
from math import ceil

T = TypeVar('T')

class PaginatedResponse(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    page_size: int
    total_pages: int

async def paginate(
    query,
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100)
):
    # Count total
    count_query = select(func.count()).select_from(query.subquery())
    total = await db.scalar(count_query)

    # Get page items
    offset = (page - 1) * page_size
    items_query = query.offset(offset).limit(page_size)
    items = await db.execute(items_query)

    return PaginatedResponse(
        items=items.scalars().all(),
        total=total,
        page=page,
        page_size=page_size,
        total_pages=ceil(total / page_size)
    )

@app.get("/items/", response_model=PaginatedResponse[Item])
async def get_items(
    page: int = 1,
    page_size: int = 10,
    db: AsyncSession = Depends(get_db)
):
    query = select(Item).order_by(Item.created_at.desc())
    return await paginate(query, page, page_size)
```

### Q30: How do you integrate third-party APIs like Adobe PDF Services or Veeva Vault?
**Answer:**
```python
import httpx
from fastapi import BackgroundTasks

class AdobePDFService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://pdf-services.adobe.io"

    async def create_pdf(self, html_content: str) -> bytes:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/operation/htmltopdf",
                headers={"Authorization": f"Bearer {self.api_key}"},
                json={"html": html_content}
            )
            response.raise_for_status()
            return response.content

class VeevaVaultService:
    def __init__(self, vault_url: str, session_id: str):
        self.vault_url = vault_url
        self.session_id = session_id

    async def get_document(self, doc_id: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.vault_url}/api/v21.1/objects/documents/{doc_id}",
                headers={"Authorization": self.session_id}
            )
            response.raise_for_status()
            return response.json()

# Using in endpoints
@app.post("/generate-pdf/")
async def generate_pdf(
    content: str,
    background_tasks: BackgroundTasks,
    pdf_service: AdobePDFService = Depends()
):
    pdf_bytes = await pdf_service.create_pdf(content)

    # Save to storage in background
    background_tasks.add_task(save_pdf_to_storage, pdf_bytes)

    return {"status": "PDF generated", "size": len(pdf_bytes)}

@app.get("/veeva/document/{doc_id}")
async def get_veeva_document(
    doc_id: str,
    veeva_service: VeevaVaultService = Depends()
):
    document = await veeva_service.get_document(doc_id)
    return document
```

---

## Common Interview Questions

### Q31: What are the main differences between FastAPI and Flask?
**Key Differences:**
1. **Performance:** FastAPI is faster (async support)
2. **Type Hints:** FastAPI uses Pydantic for validation
3. **Documentation:** Auto-generated OpenAPI docs
4. **Async:** Native async/await support
5. **Validation:** Automatic request/response validation

### Q32: How do you ensure API security in FastAPI?
**Security Measures:**
1. Authentication (JWT, OAuth2)
2. Authorization (role-based access)
3. Input validation (Pydantic)
4. Rate limiting
5. CORS configuration
6. HTTPS only
7. SQL injection prevention (parameterized queries)
8. Secrets management

### Q33: What is the N+1 query problem and how do you solve it in FastAPI?
**Answer:**
```python
# Problem: N+1 queries
@app.get("/users/")
async def get_users_with_posts(db: AsyncSession = Depends(get_db)):
    users = await db.execute(select(User))
    result = []
    for user in users.scalars():
        # This creates N additional queries!
        posts = await db.execute(select(Post).filter(Post.user_id == user.id))
        result.append({"user": user, "posts": posts.scalars().all()})
    return result

# Solution: Use eager loading
from sqlalchemy.orm import selectinload

@app.get("/users/")
async def get_users_with_posts_optimized(db: AsyncSession = Depends(get_db)):
    users = await db.execute(
        select(User).options(selectinload(User.posts))
    )
    return users.scalars().all()
```

---

## Best Practices Summary

1. **Always use async/await for I/O operations**
2. **Use Pydantic for validation**
3. **Implement proper error handling**
4. **Use dependency injection**
5. **Structure your project properly**
6. **Write tests**
7. **Use connection pooling**
8. **Implement caching**
9. **Monitor and log everything**
10. **Use type hints everywhere**

---

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [SQLAlchemy Async](https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html)
- [Uvicorn](https://www.uvicorn.org/)
