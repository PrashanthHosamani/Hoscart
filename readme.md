# 🛒 Hoscart – Production-Ready E-Commerce Backend API

Hoscart is a scalable and production-oriented E-Commerce Backend built using Django REST Framework. The project was developed with a strong focus on backend engineering principles rather than simply implementing CRUD operations.

The goal of the project is to simulate how modern e-commerce platforms handle authentication, product management, shopping carts, orders, payments, caching, and deployment in a real-world production environment.

---

# 🎯 Project Objective

The primary objective of Hoscart is to understand and implement the core backend architecture behind large-scale e-commerce platforms.

The project focuses on:

- Designing scalable REST APIs
- Database modeling and relationships
- Authentication and authorization
- Order processing workflows
- Payment integration
- Caching and performance optimization
- Production deployment
- Clean and maintainable backend architecture

---

# 🚀 Key Features

## 🔐 Authentication & Authorization

- User Registration
- User Login
- JWT Authentication
- Access Token & Refresh Token
- Protected Endpoints
- User-specific Data Access
- Secure API Communication

---

## 📦 Product Management

- Product Creation
- Product Listing
- Product Detail Retrieval
- Product Update
- Product Deletion
- Product Categories
- Product Images
- Product Search
- Product Filtering
- Product Pagination

---

## 🛒 Shopping Cart System

- Add Products to Cart
- Update Cart Item Quantity
- Remove Products from Cart
- Retrieve User Cart
- Cart Total Calculation
- Stock Validation
- Duplicate Item Prevention
- User-specific Cart Isolation

---

## 📋 Order Management

- Create Orders from Cart
- Order Item Snapshot Storage
- Order History
- Order Details
- Order Status Tracking
- Automatic Cart Cleanup after Order Placement

### Supported Order Statuses

- Pending
- Paid
- Cancelled
- Refunded
- Failed

---

## 💳 Payment Integration

- Stripe Payment Gateway
- Payment Intent Creation
- Payment Verification
- Order Payment Tracking
- Failed Payment Handling
- Successful Payment Confirmation

---

## ❤️ Wishlist System

- Add Product to Wishlist
- Remove Product from Wishlist
- User-specific Wishlist
- Retrieve Wishlist

---

## ⭐ Product Reviews & Ratings

- Product Ratings
- Product Reviews
- Average Rating Calculation
- User-specific Review Restrictions

---

## 📧 Email Notifications

- Registration Email
- Order Confirmation Email
- Payment Confirmation Email
- Password Reset Email

---

## ⚡ Performance Optimization

### Redis Caching

- Product List Caching
- Product Detail Caching
- Category Caching
- Frequently Accessed Data Caching

### Query Optimization

- select_related()
- prefetch_related()
- Database Query Reduction

### Pagination

- Limit Offset Pagination
- Optimized Response Sizes

---

## 🐳 Containerization

- Dockerized Application
- Docker Compose Support
- Environment-based Configuration

---

## ☁️ Deployment

- AWS EC2 Deployment
- Nginx Reverse Proxy
- Gunicorn Application Server
- PostgreSQL Production Database
- Redis Production Cache
- SSL Configuration

---

# 🏗️ System Architecture

```text
Client
│
├── Web Application
├── Mobile Application
└── Postman
        │
        ▼
Django REST Framework
        │
        ▼
Business Logic Layer
        │
 ┌──────┴──────┐
 ▼             ▼
PostgreSQL    Redis
(Database)    (Cache)
        │
        ▼
Stripe Payment Gateway
        │
        ▼
Email Service
```

---

# 🛠️ Technology Stack

## Backend

- Python
- Django
- Django REST Framework

## Database

- PostgreSQL

## Authentication

- JWT Authentication
- Simple JWT

## Caching

- Redis

## Payment Processing

- Stripe

## Deployment

- AWS EC2
- Nginx
- Gunicorn

## Containerization

- Docker
- Docker Compose

## Version Control

- Git
- GitHub

---

# 📂 Project Structure

```text
hoscart/
│
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── store/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── cart/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── orders/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── wishlist/
│
├── reviews/
│
├── payments/
│
├── notifications/
│
├── hoscart/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py
```

---

# 🗄️ Database Design

## Account

Stores user information and authentication details.

### Relationships

```text
Account
 │
 ├── Cart
 ├── Orders
 ├── Wishlist
 └── Reviews
```

---

## Product

Stores all product-related information.

### Relationships

```text
Category
   │
   ▼
 Product
   │
   ├── Cart Items
   ├── Order Items
   ├── Reviews
   └── Wishlist Items
```

---

## Cart

Stores active shopping cart data.

### Relationships

```text
User
 │
 ▼
Cart
 │
 ▼
CartItems
```

---

## Orders

Stores finalized purchase information.

### Relationships

```text
User
 │
 ▼
Order
 │
 ▼
OrderItems
```

---

# 🔥 Important Backend Concepts Implemented

## JWT Authentication

Implemented secure authentication using Access and Refresh Tokens.

Benefits:

- Stateless Authentication
- Scalable Architecture
- Better API Security

---

## Order Snapshot Pattern

At order creation:

```text
Product Name
Product Price
Quantity
```

are copied into OrderItems.

This ensures:

- Historical Accuracy
- Order Integrity
- Product Change Independence

---

## Database Transactions

Implemented using:

```python
transaction.atomic()
```

Benefits:

- Prevent Partial Order Creation
- Maintain Data Consistency
- Automatic Rollback on Failure

---

## Redis Caching

Used to reduce database hits and improve API performance.

Benefits:

- Faster Response Times
- Reduced Database Load
- Improved Scalability

---

# 📡 API Endpoints

## Authentication

| Method | Endpoint | Description |
|----------|----------|-------------|
| POST | /api/register/ | Register User |
| POST | /api/login/ | Login User |
| POST | /api/token/refresh/ | Refresh JWT |

---

## Products

| Method | Endpoint |
|----------|----------|
| GET | /api/products/ |
| GET | /api/products/<id>/ |
| POST | /api/products/ |
| PATCH | /api/products/<id>/ |
| DELETE | /api/products/<id>/ |

---

## Cart

| Method | Endpoint |
|----------|----------|
| GET | /api/cart/ |
| POST | /api/cart/add/ |
| PATCH | /api/cart/update/<id>/ |
| DELETE | /api/cart/remove/<id>/ |

---

## Orders

| Method | Endpoint |
|----------|----------|
| POST | /api/orders/ |
| GET | /api/orders/ |
| GET | /api/orders/<id>/ |

---

## Wishlist

| Method | Endpoint |
|----------|----------|
| GET | /api/wishlist/ |
| POST | /api/wishlist/add/ |
| DELETE | /api/wishlist/remove/<id>/ |

---

## Reviews

| Method | Endpoint |
|----------|----------|
| GET | /api/reviews/ |
| POST | /api/reviews/ |

---

## Payments

| Method | Endpoint |
|----------|----------|
| POST | /api/payment/create/ |
| POST | /api/payment/verify/ |

---

# 🚀 Local Setup

## Clone Repository

```bash
git clone https://github.com/your-username/hoscart.git
cd hoscart
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

### Activate

Windows

```bash
.venv\Scripts\activate
```

Mac/Linux

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create `.env`

```env
SECRET_KEY=your_secret_key

DEBUG=True

DATABASE_NAME=hoscart
DATABASE_USER=postgres
DATABASE_PASSWORD=password

STRIPE_SECRET_KEY=your_key

REDIS_URL=redis://localhost:6379
```

---

## Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

---

## Start Server

```bash
python manage.py runserver
```

---

# 🧪 Testing

Run all tests:

```bash
python manage.py test
```

---

# 📈 Future Improvements

- Recommendation System
- Inventory Management
- Coupon System
- Multi-Vendor Marketplace
- Analytics Dashboard
- Elasticsearch Integration
- Asynchronous Tasks using Celery
- Kafka Event Streaming
- Microservices Migration

---

# 📚 What I Learned

Through Hoscart, I gained hands-on experience with:

- Backend System Design
- Django REST Framework
- Authentication & Authorization
- Database Modeling
- PostgreSQL
- Redis Caching
- AWS Deployment
- Docker
- Payment Integration
- Transaction Management
- REST API Design
- Performance Optimization
- Production Deployment Practices

---


# ⭐ Final Note

Hoscart was built as a backend engineering project to understand how production-grade e-commerce systems are designed, optimized, secured, and deployed. The project focuses not only on functionality but also on scalability, maintainability, and real-world software engineering practices.