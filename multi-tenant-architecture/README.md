# Multi-Tenant Architecture Interview Questions & Guide

## Table of Contents
1. [Multi-Tenancy Fundamentals](#multi-tenancy-fundamentals)
2. [Isolation Strategies](#isolation-strategies)
3. [Data Architecture Patterns](#data-architecture-patterns)
4. [Security & Access Control](#security--access-control)
5. [Scalability & Performance](#scalability--performance)
6. [Implementation in Python/FastAPI](#implementation-in-pythonfastapi)
7. [Azure Multi-Tenant Patterns](#azure-multi-tenant-patterns)
8. [Common Challenges & Solutions](#common-challenges--solutions)

---

## Multi-Tenancy Fundamentals

### Q1: What is multi-tenancy and why is it important?
**Answer:**
Multi-tenancy is an architecture where a single instance of software serves multiple customers (tenants). Each tenant's data is isolated and invisible to other tenants.

**Benefits:**
- **Cost Efficiency:** Shared infrastructure reduces per-tenant costs
- **Easier Maintenance:** Single codebase and infrastructure
- **Scalability:** Can serve thousands of customers
- **Faster Deployment:** New tenants can be onboarded quickly

**Use Cases:**
- SaaS applications (Salesforce, Slack, Microsoft 365)
- Healthcare platforms (multiple hospitals)
- E-commerce platforms (multi-store)
- B2B applications

**Example:**
```python
# Tenant context
class TenantContext:
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id
        self.schema = f"tenant_{tenant_id}"

# Usage
tenant_a = TenantContext("company_a")
tenant_b = TenantContext("company_b")
```

### Q2: What are the different types of multi-tenancy models?
**Answer:**

**1. Database per Tenant (Siloed)**
- Each tenant has its own database
- Maximum isolation
- Higher cost per tenant
- Easier compliance

**2. Schema per Tenant (Isolated)**
- Shared database, separate schemas
- Good isolation
- Moderate cost
- Complex queries across tenants

**3. Shared Schema (Shared)**
- All tenants share same tables
- Lowest cost
- Highest scalability
- Requires careful implementation

**Comparison:**

| Model | Isolation | Cost | Scalability | Complexity |
|-------|-----------|------|-------------|------------|
| Database per Tenant | High | High | Low | Low |
| Schema per Tenant | Medium | Medium | Medium | Medium |
| Shared Schema | Low | Low | High | High |

### Q3: How do you choose the right multi-tenancy model?
**Answer:**

**Factors to Consider:**
1. **Data Sensitivity:** Higher sensitivity → More isolation
2. **Compliance Requirements:** HIPAA, GDPR → Database per tenant
3. **Number of Tenants:** Many tenants → Shared schema
4. **Customization Needs:** High customization → Schema per tenant
5. **Budget:** Lower budget → Shared schema
6. **Performance Requirements:** Predictable performance → Database per tenant

**Decision Matrix:**
```python
def choose_tenancy_model(
    data_sensitivity: str,  # "low", "medium", "high"
    tenant_count: int,
    customization: str,     # "low", "high"
    budget: str             # "low", "high"
) -> str:
    if data_sensitivity == "high" or customization == "high":
        return "database_per_tenant"
    elif tenant_count < 100 and budget == "high":
        return "schema_per_tenant"
    else:
        return "shared_schema"
```

---

## Isolation Strategies

### Q4: How do you implement data isolation in a shared schema model?
**Answer:**

**1. Tenant ID Column:**
```python
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    tenant_id = Column(String, nullable=False, index=True)
    username = Column(String)
    email = Column(String)

    # Composite index for performance
    __table_args__ = (
        Index('idx_tenant_user', 'tenant_id', 'id'),
    )

# Query with tenant filter
async def get_users(db: AsyncSession, tenant_id: str):
    result = await db.execute(
        select(User).filter(User.tenant_id == tenant_id)
    )
    return result.scalars().all()
```

**2. Row-Level Security (PostgreSQL):**
```sql
-- Enable RLS
ALTER TABLE users ENABLE ROW LEVEL SECURITY;

-- Create policy
CREATE POLICY tenant_isolation_policy ON users
    USING (tenant_id = current_setting('app.current_tenant')::text);

-- Set tenant context
SET app.current_tenant = 'tenant_123';
SELECT * FROM users;  -- Only returns tenant_123's data
```

**3. ORM-Level Filtering:**
```python
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

class TenantSession:
    def __init__(self, session: AsyncSession, tenant_id: str):
        self.session = session
        self.tenant_id = tenant_id

    async def query(self, model):
        return await self.session.execute(
            select(model).filter(model.tenant_id == self.tenant_id)
        )

# FastAPI dependency
async def get_tenant_session(
    tenant_id: str = Depends(get_tenant_id),
    db: AsyncSession = Depends(get_db)
) -> TenantSession:
    return TenantSession(db, tenant_id)
```

### Q5: How do you implement tenant identification and context?
**Answer:**

**1. Subdomain-based:**
```python
from fastapi import Request, HTTPException

async def extract_tenant_from_subdomain(request: Request) -> str:
    host = request.headers.get("host", "")
    # Extract: tenant1.myapp.com -> tenant1
    parts = host.split(".")
    if len(parts) < 3:
        raise HTTPException(status_code=400, detail="Invalid subdomain")
    return parts[0]

@app.get("/data")
async def get_data(tenant_id: str = Depends(extract_tenant_from_subdomain)):
    return {"tenant": tenant_id, "data": [...]}
```

**2. Header-based:**
```python
from fastapi import Header

async def get_tenant_from_header(
    x_tenant_id: str = Header(..., alias="X-Tenant-ID")
) -> str:
    if not await validate_tenant(x_tenant_id):
        raise HTTPException(status_code=400, detail="Invalid tenant")
    return x_tenant_id
```

**3. JWT Token-based:**
```python
from jose import jwt

async def get_tenant_from_token(
    token: str = Depends(oauth2_scheme)
) -> str:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    tenant_id = payload.get("tenant_id")
    if not tenant_id:
        raise HTTPException(status_code=401, detail="No tenant in token")
    return tenant_id
```

**4. URL Path-based:**
```python
@app.get("/tenants/{tenant_id}/users")
async def get_tenant_users(tenant_id: str):
    # Validate user has access to this tenant
    await verify_tenant_access(tenant_id, current_user)
    return await get_users(tenant_id)
```

### Q6: How do you prevent cross-tenant data leakage?
**Answer:**

**1. Always Filter by Tenant ID:**
```python
# Bad - no tenant filter
async def get_user_bad(user_id: int, db: AsyncSession):
    return await db.get(User, user_id)  # Can access any tenant!

# Good - with tenant filter
async def get_user_good(
    user_id: int,
    tenant_id: str,
    db: AsyncSession
):
    result = await db.execute(
        select(User).filter(
            User.id == user_id,
            User.tenant_id == tenant_id
        )
    )
    return result.scalar_one_or_none()
```

**2. Database Views:**
```sql
-- Create tenant-specific view
CREATE VIEW tenant_users AS
SELECT *
FROM users
WHERE tenant_id = current_setting('app.current_tenant')::text;

-- Revoke access to base table
REVOKE ALL ON users FROM app_role;
GRANT SELECT ON tenant_users TO app_role;
```

**3. Automated Testing:**
```python
import pytest

@pytest.mark.parametrize("tenant_id", ["tenant_a", "tenant_b"])
async def test_tenant_isolation(tenant_id: str):
    # Create data for tenant A
    user_a = await create_user("tenant_a", "user_a")

    # Try to access with tenant B context
    with pytest.raises(Exception):
        await get_user(user_a.id, "tenant_b")
```

**4. Database Triggers:**
```sql
-- Prevent updates to wrong tenant
CREATE OR REPLACE FUNCTION check_tenant_access()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.tenant_id != current_setting('app.current_tenant')::text THEN
        RAISE EXCEPTION 'Cannot modify data for different tenant';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER enforce_tenant_access
    BEFORE UPDATE ON users
    FOR EACH ROW EXECUTE FUNCTION check_tenant_access();
```

---

## Data Architecture Patterns

### Q7: How do you design a scalable multi-tenant database schema?
**Answer:**

**1. Shared Schema with Tenant ID:**
```sql
-- Core tables
CREATE TABLE tenants (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    subdomain VARCHAR(100) UNIQUE NOT NULL,
    tier VARCHAR(50),  -- free, pro, enterprise
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    settings JSONB
);

CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenants(id),
    username VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(tenant_id, email),
    UNIQUE(tenant_id, username)
);

CREATE INDEX idx_users_tenant ON users(tenant_id, id);
CREATE INDEX idx_users_email ON users(tenant_id, email);

CREATE TABLE products (
    id BIGSERIAL PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenants(id),
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_products_tenant ON products(tenant_id);
```

**2. Partitioning Strategy:**
```sql
-- Partition by tenant for large tables
CREATE TABLE orders (
    id BIGSERIAL,
    tenant_id UUID NOT NULL,
    user_id BIGINT,
    total DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) PARTITION BY LIST (tenant_id);

-- Create partitions per tenant (or group of tenants)
CREATE TABLE orders_tenant_a PARTITION OF orders
    FOR VALUES IN ('tenant-a-uuid');

CREATE TABLE orders_tenant_b PARTITION OF orders
    FOR VALUES IN ('tenant-b-uuid');

-- Default partition for new tenants
CREATE TABLE orders_default PARTITION OF orders DEFAULT;
```

**3. Separate Schemas (PostgreSQL):**
```sql
-- Create schemas per tenant
CREATE SCHEMA tenant_a;
CREATE SCHEMA tenant_b;

-- Set search path based on tenant
SET search_path TO tenant_a;

-- Create tables (same structure in each schema)
CREATE TABLE tenant_a.users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(255)
);
```

### Q8: How do you handle tenant-specific customizations?
**Answer:**

**1. Configuration Tables:**
```python
from sqlalchemy import Column, String, JSON
from sqlalchemy.dialects.postgresql import JSONB

class TenantConfig(Base):
    __tablename__ = "tenant_configs"

    tenant_id = Column(String, primary_key=True)
    custom_fields = Column(JSONB, default={})
    branding = Column(JSONB, default={})
    features = Column(JSONB, default={})
    limits = Column(JSONB, default={})

# Usage
async def get_tenant_config(tenant_id: str, db: AsyncSession):
    result = await db.execute(
        select(TenantConfig).filter(TenantConfig.tenant_id == tenant_id)
    )
    return result.scalar_one_or_none()

@app.get("/users/")
async def get_users(
    tenant_id: str = Depends(get_tenant_id),
    config: TenantConfig = Depends(get_tenant_config)
):
    # Apply tenant-specific logic
    if config.features.get("advanced_search"):
        return await advanced_user_search()
    else:
        return await basic_user_search()
```

**2. EAV (Entity-Attribute-Value) Pattern:**
```python
class CustomField(Base):
    __tablename__ = "custom_fields"

    id = Column(Integer, primary_key=True)
    tenant_id = Column(String, nullable=False)
    entity_type = Column(String)  # "user", "product", etc.
    entity_id = Column(Integer)
    field_name = Column(String)
    field_value = Column(String)

# Query custom fields
async def get_entity_with_custom_fields(
    entity_type: str,
    entity_id: int,
    tenant_id: str,
    db: AsyncSession
):
    # Get base entity
    entity = await get_entity(entity_type, entity_id, tenant_id, db)

    # Get custom fields
    custom_fields = await db.execute(
        select(CustomField).filter(
            CustomField.tenant_id == tenant_id,
            CustomField.entity_type == entity_type,
            CustomField.entity_id == entity_id
        )
    )

    # Merge
    entity.custom_fields = {
        cf.field_name: cf.field_value
        for cf in custom_fields.scalars()
    }

    return entity
```

**3. JSONB Columns:**
```python
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    tenant_id = Column(String, nullable=False)
    name = Column(String)
    price = Column(Float)
    custom_data = Column(JSONB, default={})  # Tenant-specific fields

# Query JSONB fields
@app.get("/products/")
async def search_products(
    category: Optional[str] = None,
    tenant_id: str = Depends(get_tenant_id)
):
    query = select(Product).filter(Product.tenant_id == tenant_id)

    if category:
        # Query JSONB field
        query = query.filter(
            Product.custom_data['category'].astext == category
        )

    result = await db.execute(query)
    return result.scalars().all()
```

### Q9: How do you handle tenant migrations and schema evolution?
**Answer:**

**1. Version-aware Migrations:**
```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Add column to all tenant schemas
    for schema in get_tenant_schemas():
        with op.batch_alter_table("users", schema=schema) as batch_op:
            batch_op.add_column(
                sa.Column('phone', sa.String(20), nullable=True)
            )

def downgrade():
    for schema in get_tenant_schemas():
        with op.batch_alter_table("users", schema=schema) as batch_op:
            batch_op.drop_column('phone')
```

**2. Zero-Downtime Migrations:**
```python
# Phase 1: Add nullable column
def upgrade_phase_1():
    op.add_column('users',
        sa.Column('new_field', sa.String(100), nullable=True))

# Phase 2: Backfill data
def upgrade_phase_2():
    # Update in batches to avoid locking
    op.execute("""
        UPDATE users
        SET new_field = old_field
        WHERE new_field IS NULL
        LIMIT 1000
    """)

# Phase 3: Make column non-nullable
def upgrade_phase_3():
    op.alter_column('users', 'new_field', nullable=False)

# Phase 4: Drop old column
def upgrade_phase_4():
    op.drop_column('users', 'old_field')
```

**3. Tenant-specific Migrations:**
```python
class TenantMigration(Base):
    __tablename__ = "tenant_migrations"

    tenant_id = Column(String, primary_key=True)
    version = Column(Integer, primary_key=True)
    applied_at = Column(DateTime, default=datetime.utcnow)

async def apply_tenant_migration(
    tenant_id: str,
    version: int,
    migration_func
):
    # Check if already applied
    existing = await db.execute(
        select(TenantMigration).filter(
            TenantMigration.tenant_id == tenant_id,
            TenantMigration.version == version
        )
    )

    if existing.scalar_one_or_none():
        return

    # Apply migration
    await migration_func(tenant_id)

    # Record migration
    db.add(TenantMigration(tenant_id=tenant_id, version=version))
    await db.commit()
```

---

## Security & Access Control

### Q10: How do you implement role-based access control (RBAC) in a multi-tenant system?
**Answer:**

```python
from enum import Enum

class Role(str, Enum):
    TENANT_ADMIN = "tenant_admin"
    USER = "user"
    VIEWER = "viewer"

class Permission(str, Enum):
    READ_USERS = "read:users"
    WRITE_USERS = "write:users"
    DELETE_USERS = "delete:users"
    MANAGE_TENANT = "manage:tenant"

# Role-Permission mapping
ROLE_PERMISSIONS = {
    Role.TENANT_ADMIN: [
        Permission.READ_USERS,
        Permission.WRITE_USERS,
        Permission.DELETE_USERS,
        Permission.MANAGE_TENANT
    ],
    Role.USER: [
        Permission.READ_USERS,
        Permission.WRITE_USERS
    ],
    Role.VIEWER: [
        Permission.READ_USERS
    ]
}

# Database models
class TenantUser(Base):
    __tablename__ = "tenant_users"

    id = Column(Integer, primary_key=True)
    tenant_id = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)
    role = Column(Enum(Role), nullable=False)

# Permission checking
async def has_permission(
    user: User,
    tenant_id: str,
    permission: Permission,
    db: AsyncSession
) -> bool:
    # Get user's role in tenant
    tenant_user = await db.execute(
        select(TenantUser).filter(
            TenantUser.user_id == user.id,
            TenantUser.tenant_id == tenant_id
        )
    )
    tenant_user = tenant_user.scalar_one_or_none()

    if not tenant_user:
        return False

    # Check if role has permission
    return permission in ROLE_PERMISSIONS[tenant_user.role]

# FastAPI dependency
async def require_permission(permission: Permission):
    async def permission_checker(
        tenant_id: str = Depends(get_tenant_id),
        user: User = Depends(get_current_user),
        db: AsyncSession = Depends(get_db)
    ):
        if not await has_permission(user, tenant_id, permission, db):
            raise HTTPException(
                status_code=403,
                detail=f"Permission denied: {permission}"
            )
        return True

    return permission_checker

# Usage
@app.delete("/users/{user_id}")
async def delete_user(
    user_id: int,
    _: bool = Depends(require_permission(Permission.DELETE_USERS))
):
    await delete_user_from_db(user_id)
    return {"status": "deleted"}
```

### Q11: How do you implement tenant-level rate limiting?
**Answer:**

```python
import redis.asyncio as redis
from datetime import datetime, timedelta

class TenantRateLimiter:
    def __init__(self, redis_client: redis.Redis):
        self.redis = redis_client

    async def check_rate_limit(
        self,
        tenant_id: str,
        endpoint: str,
        max_requests: int,
        window_seconds: int
    ) -> bool:
        key = f"rate_limit:{tenant_id}:{endpoint}"
        now = datetime.utcnow()
        window_start = now - timedelta(seconds=window_seconds)

        # Remove old requests
        await self.redis.zremrangebyscore(
            key,
            0,
            window_start.timestamp()
        )

        # Count requests in window
        request_count = await self.redis.zcard(key)

        if request_count >= max_requests:
            return False

        # Add current request
        await self.redis.zadd(
            key,
            {str(now): now.timestamp()}
        )

        # Set expiry
        await self.redis.expire(key, window_seconds)

        return True

# Tier-based limits
TIER_LIMITS = {
    "free": {"requests_per_hour": 100},
    "pro": {"requests_per_hour": 1000},
    "enterprise": {"requests_per_hour": 10000}
}

async def check_tenant_rate_limit(
    request: Request,
    tenant_id: str = Depends(get_tenant_id),
    tenant_config: TenantConfig = Depends(get_tenant_config),
    limiter: TenantRateLimiter = Depends(get_rate_limiter)
):
    tier = tenant_config.tier
    max_requests = TIER_LIMITS[tier]["requests_per_hour"]

    endpoint = request.url.path

    if not await limiter.check_rate_limit(
        tenant_id,
        endpoint,
        max_requests,
        3600  # 1 hour
    ):
        raise HTTPException(
            status_code=429,
            detail=f"Rate limit exceeded for tier {tier}"
        )

# Usage
@app.get("/api/data")
async def get_data(
    _: None = Depends(check_tenant_rate_limit)
):
    return {"data": [...]}
```

---

## Scalability & Performance

### Q12: How do you optimize database queries in a multi-tenant system?
**Answer:**

**1. Proper Indexing:**
```sql
-- Composite indexes for tenant-specific queries
CREATE INDEX idx_users_tenant_id ON users(tenant_id, id);
CREATE INDEX idx_users_tenant_email ON users(tenant_id, email);
CREATE INDEX idx_products_tenant_created ON products(tenant_id, created_at DESC);

-- Partial indexes for specific tenant tiers
CREATE INDEX idx_enterprise_tenants ON tenants(id)
WHERE tier = 'enterprise';
```

**2. Query Optimization:**
```python
from sqlalchemy import func, and_

# Bad: N+1 query
async def get_users_with_orders_bad(tenant_id: str):
    users = await db.execute(
        select(User).filter(User.tenant_id == tenant_id)
    )
    result = []
    for user in users.scalars():
        orders = await db.execute(
            select(Order).filter(Order.user_id == user.id)
        )
        result.append({
            "user": user,
            "orders": orders.scalars().all()
        })
    return result

# Good: JOIN with eager loading
async def get_users_with_orders_good(tenant_id: str):
    result = await db.execute(
        select(User)
        .options(selectinload(User.orders))
        .filter(User.tenant_id == tenant_id)
    )
    return result.scalars().all()

# Even better: Aggregate in database
async def get_users_with_order_count(tenant_id: str):
    result = await db.execute(
        select(
            User,
            func.count(Order.id).label('order_count')
        )
        .outerjoin(Order)
        .filter(User.tenant_id == tenant_id)
        .group_by(User.id)
    )
    return result.all()
```

**3. Caching Strategy:**
```python
import json
from typing import Optional

class TenantCache:
    def __init__(self, redis_client: redis.Redis):
        self.redis = redis_client

    async def get(self, tenant_id: str, key: str) -> Optional[dict]:
        cache_key = f"tenant:{tenant_id}:{key}"
        data = await self.redis.get(cache_key)
        return json.loads(data) if data else None

    async def set(
        self,
        tenant_id: str,
        key: str,
        value: dict,
        ttl: int = 300
    ):
        cache_key = f"tenant:{tenant_id}:{key}"
        await self.redis.setex(
            cache_key,
            ttl,
            json.dumps(value)
        )

    async def invalidate(self, tenant_id: str, pattern: str = "*"):
        keys = await self.redis.keys(f"tenant:{tenant_id}:{pattern}")
        if keys:
            await self.redis.delete(*keys)

# Usage
@app.get("/users/")
async def get_users(
    tenant_id: str = Depends(get_tenant_id),
    cache: TenantCache = Depends(get_cache)
):
    # Try cache first
    cached = await cache.get(tenant_id, "users")
    if cached:
        return cached

    # Query database
    users = await get_users_from_db(tenant_id)

    # Cache result
    await cache.set(tenant_id, "users", users, ttl=300)

    return users
```

### Q13: How do you handle tenant onboarding and provisioning at scale?
**Answer:**

```python
from enum import Enum
from datetime import datetime

class ProvisioningStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

class TenantProvisioning(Base):
    __tablename__ = "tenant_provisioning"

    tenant_id = Column(String, primary_key=True)
    status = Column(Enum(ProvisioningStatus), default=ProvisioningStatus.PENDING)
    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    error_message = Column(String)

# Provisioning workflow
async def provision_tenant(tenant_id: str, config: dict):
    provisioning = TenantProvisioning(
        tenant_id=tenant_id,
        status=ProvisioningStatus.IN_PROGRESS,
        started_at=datetime.utcnow()
    )
    await db.add(provisioning)
    await db.commit()

    try:
        # Step 1: Create database schema/tables
        await create_tenant_schema(tenant_id)

        # Step 2: Initialize default data
        await initialize_tenant_data(tenant_id, config)

        # Step 3: Setup storage (S3 bucket, etc.)
        await setup_tenant_storage(tenant_id)

        # Step 4: Configure services
        await configure_tenant_services(tenant_id, config)

        # Step 5: Create admin user
        await create_admin_user(tenant_id, config.get('admin_email'))

        # Mark as completed
        provisioning.status = ProvisioningStatus.COMPLETED
        provisioning.completed_at = datetime.utcnow()
        await db.commit()

        # Send welcome email
        await send_welcome_email(tenant_id)

    except Exception as e:
        provisioning.status = ProvisioningStatus.FAILED
        provisioning.error_message = str(e)
        await db.commit()
        raise

# Background job for provisioning
from celery import Celery

celery_app = Celery('tasks', broker='redis://localhost:6379')

@celery_app.task
def provision_tenant_async(tenant_id: str, config: dict):
    asyncio.run(provision_tenant(tenant_id, config))

# API endpoint
@app.post("/tenants/")
async def create_tenant(
    name: str,
    subdomain: str,
    admin_email: str,
    tier: str = "free"
):
    # Create tenant record
    tenant = Tenant(
        name=name,
        subdomain=subdomain,
        tier=tier
    )
    db.add(tenant)
    await db.commit()

    # Start provisioning in background
    provision_tenant_async.delay(
        str(tenant.id),
        {
            "admin_email": admin_email,
            "tier": tier
        }
    )

    return {
        "tenant_id": tenant.id,
        "status": "provisioning",
        "message": "Tenant is being provisioned"
    }
```

---

## Implementation in Python/FastAPI

### Q14: Show a complete FastAPI multi-tenant implementation
**Answer:**

```python
# main.py
from fastapi import FastAPI, Depends, HTTPException, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager
import redis.asyncio as redis

# Database setup
DATABASE_URL = "postgresql+asyncpg://user:pass@localhost/mydb"
engine = create_async_engine(DATABASE_URL, pool_size=20)
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Redis setup
redis_client = redis.from_url("redis://localhost")

# App setup
app = FastAPI(title="Multi-Tenant API")

# Dependencies
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

async def get_redis():
    return redis_client

async def get_tenant_id(
    request: Request,
    x_tenant_id: str = Header(None, alias="X-Tenant-ID")
) -> str:
    # Try header first
    if x_tenant_id:
        tenant_id = x_tenant_id
    # Try subdomain
    else:
        host = request.headers.get("host", "")
        tenant_id = host.split(".")[0]

    # Validate tenant exists
    if not await validate_tenant(tenant_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid or inactive tenant"
        )

    return tenant_id

# Middleware for tenant context
@app.middleware("http")
async def tenant_context_middleware(request: Request, call_next):
    # Extract tenant ID
    try:
        tenant_id = await get_tenant_id(request)
        request.state.tenant_id = tenant_id
    except HTTPException:
        pass

    response = await call_next(request)
    return response

# Routes
from routers import users, products

app.include_router(
    users.router,
    prefix="/api/users",
    tags=["users"],
    dependencies=[Depends(get_tenant_id)]
)

app.include_router(
    products.router,
    prefix="/api/products",
    tags=["products"],
    dependencies=[Depends(get_tenant_id)]
)

# routers/users.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

router = APIRouter()

@router.get("/", response_model=List[UserResponse])
async def get_users(
    tenant_id: str = Depends(get_tenant_id),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
    skip: int = 0,
    limit: int = 100
):
    # Verify user has access to this tenant
    await verify_tenant_access(current_user, tenant_id)

    # Query users for this tenant
    result = await db.execute(
        select(User)
        .filter(User.tenant_id == tenant_id)
        .offset(skip)
        .limit(limit)
    )

    return result.scalars().all()

@router.post("/", response_model=UserResponse)
async def create_user(
    user_data: UserCreate,
    tenant_id: str = Depends(get_tenant_id),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Check permissions
    if not await has_permission(current_user, tenant_id, Permission.WRITE_USERS, db):
        raise HTTPException(status_code=403, detail="Permission denied")

    # Create user
    user = User(
        tenant_id=tenant_id,
        **user_data.dict()
    )

    db.add(user)
    await db.commit()
    await db.refresh(user)

    return user
```

---

## Azure Multi-Tenant Patterns

### Q15: How do you implement multi-tenancy using Azure services?
**Answer:**

**1. Azure SQL Database with Elastic Pools:**
```python
# Configuration
AZURE_SQL_CONFIG = {
    "server": "myserver.database.windows.net",
    "elastic_pool": "tenant-pool",
    "admin_user": "admin",
    "admin_password": "secure_password"
}

# Create database per tenant
import pyodbc

async def create_tenant_database(tenant_id: str):
    connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={AZURE_SQL_CONFIG['server']};"
        f"DATABASE=master;"
        f"UID={AZURE_SQL_CONFIG['admin_user']};"
        f"PWD={AZURE_SQL_CONFIG['admin_password']}"
    )

    with pyodbc.connect(connection_string) as conn:
        conn.autocommit = True
        cursor = conn.cursor()

        # Create database in elastic pool
        cursor.execute(f"""
            CREATE DATABASE tenant_{tenant_id}
            (SERVICE_OBJECTIVE = ELASTIC_POOL
            (name = {AZURE_SQL_CONFIG['elastic_pool']}))
        """)

    return f"tenant_{tenant_id}"
```

**2. Azure Blob Storage with Containers:**
```python
from azure.storage.blob import BlobServiceClient

class AzureTenantStorage:
    def __init__(self, connection_string: str):
        self.blob_service = BlobServiceClient.from_connection_string(
            connection_string
        )

    async def create_tenant_container(self, tenant_id: str):
        container_name = f"tenant-{tenant_id}"
        container_client = self.blob_service.get_container_client(
            container_name
        )

        if not container_client.exists():
            container_client.create_container()

        return container_name

    async def upload_file(
        self,
        tenant_id: str,
        file_name: str,
        data: bytes
    ):
        container_name = f"tenant-{tenant_id}"
        blob_client = self.blob_service.get_blob_client(
            container=container_name,
            blob=file_name
        )

        blob_client.upload_blob(data, overwrite=True)
```

**3. Azure Key Vault for Tenant Secrets:**
```python
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

class TenantSecretsManager:
    def __init__(self, vault_url: str):
        credential = DefaultAzureCredential()
        self.client = SecretClient(
            vault_url=vault_url,
            credential=credential
        )

    async def set_tenant_secret(
        self,
        tenant_id: str,
        secret_name: str,
        secret_value: str
    ):
        secret_key = f"tenant-{tenant_id}-{secret_name}"
        self.client.set_secret(secret_key, secret_value)

    async def get_tenant_secret(
        self,
        tenant_id: str,
        secret_name: str
    ) -> str:
        secret_key = f"tenant-{tenant_id}-{secret_name}"
        secret = self.client.get_secret(secret_key)
        return secret.value
```

**4. Azure OpenAI for Tenants:**
```python
from openai import AzureOpenAI

class TenantOpenAI:
    def __init__(self, tenant_config: dict):
        self.client = AzureOpenAI(
            api_key=tenant_config['openai_api_key'],
            api_version="2024-02-01",
            azure_endpoint=tenant_config['openai_endpoint']
        )

    async def generate_completion(
        self,
        prompt: str,
        max_tokens: int = 100
    ):
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens
        )

        return response.choices[0].message.content

# Usage with tenant-specific resources
@app.post("/generate/")
async def generate_text(
    prompt: str,
    tenant_id: str = Depends(get_tenant_id),
    tenant_config: dict = Depends(get_tenant_config)
):
    openai_client = TenantOpenAI(tenant_config)
    result = await openai_client.generate_completion(prompt)

    return {"result": result}
```

---

## Common Challenges & Solutions

### Q16: How do you handle tenant data backup and restore?
**Answer:**

```python
import boto3
from datetime import datetime

class TenantBackupService:
    def __init__(self, s3_bucket: str):
        self.s3 = boto3.client('s3')
        self.bucket = s3_bucket

    async def backup_tenant_data(
        self,
        tenant_id: str,
        db: AsyncSession
    ):
        timestamp = datetime.utcnow().isoformat()
        backup_key = f"backups/{tenant_id}/{timestamp}.json"

        # Export tenant data
        data = await self.export_tenant_data(tenant_id, db)

        # Upload to S3
        self.s3.put_object(
            Bucket=self.bucket,
            Key=backup_key,
            Body=json.dumps(data),
            ServerSideEncryption='AES256'
        )

        return backup_key

    async def restore_tenant_data(
        self,
        tenant_id: str,
        backup_key: str,
        db: AsyncSession
    ):
        # Download from S3
        response = self.s3.get_object(
            Bucket=self.bucket,
            Key=backup_key
        )

        data = json.loads(response['Body'].read())

        # Restore data
        await self.import_tenant_data(tenant_id, data, db)

    async def export_tenant_data(
        self,
        tenant_id: str,
        db: AsyncSession
    ) -> dict:
        # Export all tenant tables
        export_data = {}

        for model in [User, Product, Order]:
            result = await db.execute(
                select(model).filter(model.tenant_id == tenant_id)
            )
            export_data[model.__tablename__] = [
                row.__dict__ for row in result.scalars()
            ]

        return export_data
```

### Q17: How do you implement tenant metrics and monitoring?
**Answer:**

```python
from prometheus_client import Counter, Histogram, Gauge
from datetime import datetime, timedelta

# Metrics
tenant_requests = Counter(
    'tenant_requests_total',
    'Total requests per tenant',
    ['tenant_id', 'endpoint', 'status']
)

tenant_latency = Histogram(
    'tenant_request_latency_seconds',
    'Request latency per tenant',
    ['tenant_id', 'endpoint']
)

tenant_active_users = Gauge(
    'tenant_active_users',
    'Active users per tenant',
    ['tenant_id']
)

# Middleware for metrics
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    tenant_id = getattr(request.state, 'tenant_id', 'unknown')
    endpoint = request.url.path

    start_time = time.time()

    response = await call_next(request)

    duration = time.time() - start_time

    # Record metrics
    tenant_requests.labels(
        tenant_id=tenant_id,
        endpoint=endpoint,
        status=response.status_code
    ).inc()

    tenant_latency.labels(
        tenant_id=tenant_id,
        endpoint=endpoint
    ).observe(duration)

    return response

# Update active users periodically
async def update_active_users_metrics():
    while True:
        for tenant in await get_all_tenants():
            active_count = await get_active_users_count(
                tenant.id,
                since=datetime.utcnow() - timedelta(hours=1)
            )

            tenant_active_users.labels(
                tenant_id=tenant.id
            ).set(active_count)

        await asyncio.sleep(60)  # Update every minute
```

### Q18: What are the most common pitfalls in multi-tenant systems and how do you avoid them?
**Answer:**

**1. Data Leakage:**
- Always filter by tenant_id
- Use Row-Level Security
- Automated testing for isolation
- Code reviews

**2. Performance Issues:**
- Proper indexing
- Query optimization
- Caching strategy
- Database partitioning

**3. Noisy Neighbor Problem:**
- Resource quotas per tenant
- Rate limiting
- Separate infrastructure for large tenants
- Monitoring and alerting

**4. Migration Complexity:**
- Version migrations carefully
- Test on staging tenants
- Rollback plan
- Communication with tenants

**5. Security:**
- Authentication per tenant
- API keys per tenant
- Regular security audits
- Penetration testing

---

## Best Practices Summary

1. **Always filter queries by tenant_id**
2. **Use proper indexing for multi-tenant queries**
3. **Implement row-level security where possible**
4. **Cache tenant-specific data appropriately**
5. **Monitor per-tenant metrics**
6. **Test tenant isolation rigorously**
7. **Document tenant onboarding process**
8. **Plan for tenant migrations**
9. **Implement rate limiting per tenant**
10. **Use feature flags for tenant-specific features**

---

## Resources

- [Multi-Tenant SaaS Database Tenancy Patterns](https://docs.microsoft.com/en-us/azure/sql-database/saas-tenancy-app-design-patterns)
- [AWS Multi-Tenant Architectures](https://aws.amazon.com/solutions/multi-tenant/)
- [Building Multi-Tenant Applications](https://www.nginx.com/blog/building-multitenant-applications/)
