# Hoscart – Production-Ready E-Commerce Backend API

Hoscart is a scalable, production-oriented E-Commerce Backend API built using **Django REST Framework**. The project was developed with a strong focus on real-world backend engineering principles — covering authentication, product management, shopping carts, order processing, Stripe payment integration, and full Docker-based deployment on AWS EC2.

---

## Project Objective

The primary objective of Hoscart is to deeply understand and implement the core backend architecture behind large-scale e-commerce platforms.

The project focuses on:

- Designing scalable REST APIs
- Relational database modeling with PostgreSQL
- JWT-based authentication and authorization
- Order processing with database transactions
- Stripe payment gateway integration
- Containerized deployment using Docker, Gunicorn, and Nginx
- Production deployment on AWS EC2

---

## Key Features

### Authentication & Authorization
- User Registration and Login
- JWT Authentication (Access Token + Refresh Token)
- Protected Endpoints with `IsAuthenticated` permission
- User-specific data isolation

### Product Management
- Full CRUD operations on products
- Product categories
- Product image support via media uploads
- Search by product name
- Filtering by category and price range
- Pagination support

### Shopping Cart System
- Add products to cart
- Update cart item quantity with stock validation
- Remove items from cart
- Retrieve user's cart
- Cart total calculation
- Duplicate item prevention
- User-specific cart isolation

### Order Management
- Create orders from active cart (checkout)
- **Order Snapshot Pattern** — captures product name and price at time of purchase to preserve historical accuracy
- Stock deduction on order creation
- Automatic cart cleanup after order placement
- Order history and detail retrieval
- **Database Transactions** using `atomic()` to prevent partial order creation

Supported Order Statuses: `PENDING` | `PAID` | `CANCELLED`

### Stripe Payment Integration
- Create Stripe `PaymentIntent` for a pending order
- Returns `client_secret` for secure frontend card processing
- Verify payment status directly with Stripe API
- Updates Order status to `PAID` on successful verification
- Failed payment handling

### Docker Containerization
- Multi-container setup with Docker Compose
- Django + Gunicorn (application container)
- PostgreSQL 16 (database container with persistent volume)
- Nginx (reverse proxy container)
- Environment variable injection via `.env.docker`

### AWS EC2 Deployment
- Deployed on AWS EC2 Free Tier (t2.micro)
- Nginx as reverse proxy on port 80
- Gunicorn as WSGI server
- PostgreSQL running inside Docker container
- Production settings with DEBUG=False and env-based secrets

---

## System Architecture

```
Client (Browser / Postman / Mobile App)
         |
         v
    Nginx (Port 80)
    |-- /static/  -> Serves static files directly
    |-- /media/   -> Serves media files directly
    +-- /api/*    -> Forwards to Gunicorn
              |
              v
    Gunicorn (Django App - Port 8000)
              |
       +------+------+
       v             v
  PostgreSQL       Stripe API
  (Database)    (Payment Gateway)
```

---

## Technology Stack

| Layer               | Technology                                   |
|---------------------|----------------------------------------------|
| Backend Framework   | Python, Django, Django REST Framework        |
| Authentication      | JWT via djangorestframework-simplejwt         |
| Database            | PostgreSQL 16                                |
| Payment Gateway     | Stripe                                       |
| Application Server  | Gunicorn                                     |
| Reverse Proxy       | Nginx                                        |
| Containerization    | Docker, Docker Compose                       |
| Deployment          | AWS EC2 (Free Tier)                          |
| Image Handling      | Pillow                                       |

---

## Project Structure

```
hoscart/
|
|-- accounts/           # User model, registration, login, JWT
|-- store/              # Product model, CRUD, filtering, pagination
|-- category/           # Product categories
|-- cart/               # Cart and CartItem models, add/update/remove
|-- order/              # Order and OrderItem models, checkout logic
|-- payments/           # Stripe PaymentIntent creation and verification
|
|-- hoscart/
|   |-- settings.py     # Production-ready settings (env-based)
|   |-- urls.py         # Root URL configuration
|   +-- wsgi.py
|
|-- nginx/
|   +-- nginx.conf      # Nginx reverse proxy configuration
|
|-- Dockerfile          # Django container build instructions
|-- docker-compose.yml  # Orchestrates Django + PostgreSQL + Nginx
|-- requirements.txt    # Python dependencies
+-- manage.py
```

---

## Database Design

### Key Relationships

```
Account
 |-- Cart -> CartItems -> Products
 +-- Orders -> OrderItems (snapshot of product + price)
              +-- Payment (Stripe record)

Category
 +-- Products
```

### Order Snapshot Pattern
When an order is created, the product name and price are copied into `OrderItem`. This ensures order history remains accurate even if the product is later modified or deleted.

---

## Important Backend Concepts Implemented

### Database Transactions
```python
@transaction.atomic
def create(self, validated_data):
    ...
```
Used in order creation to ensure all steps — creating the order, creating order items, deducting stock, and clearing the cart — either all succeed or all roll back together.

### JWT Authentication Flow
```
POST /api/login/ -> { access: "...", refresh: "..." }
                         |
                  Authorization: Bearer <access_token>
                         |
                  Protected API Endpoints
```

---

## API Endpoints

### Authentication

| Method | Endpoint              | Description               | Auth Required |
|--------|-----------------------|---------------------------|---------------|
| POST   | `/api/register/`      | Register new user         | No            |
| POST   | `/api/login/`         | Login and receive tokens  | No            |
| POST   | `/api/token/refresh/` | Refresh access token      | No            |

### Products

| Method | Endpoint               | Description                                    | Auth Required |
|--------|------------------------|------------------------------------------------|---------------|
| GET    | `/api/products/`       | List all products (filterable, searchable)     | Yes           |
| GET    | `/api/products/<id>/`  | Retrieve product detail                        | Yes           |
| POST   | `/api/products/`       | Create a new product                           | Yes           |
| PATCH  | `/api/products/<id>/`  | Update an existing product                     | Yes           |
| DELETE | `/api/products/<id>/`  | Delete a product                               | Yes           |

### Cart

| Method | Endpoint                    | Description                   | Auth Required |
|--------|-----------------------------|-------------------------------|---------------|
| GET    | `/api/cart/`                | Retrieve user's cart          | Yes           |
| POST   | `/api/cart/add/`            | Add a product to cart         | Yes           |
| PATCH  | `/api/cart/update/<id>/`    | Update cart item quantity     | Yes           |
| DELETE | `/api/cart/remove/<id>/`    | Remove item from cart         | Yes           |

### Orders

| Method | Endpoint              | Description                        | Auth Required |
|--------|-----------------------|------------------------------------|---------------|
| GET    | `/api/orders/`        | Retrieve order history             | Yes           |
| POST   | `/api/orders/create/` | Create order from cart (checkout)  | Yes           |
| GET    | `/api/orders/<id>/`   | Retrieve specific order detail     | Yes           |

### Payments

| Method | Endpoint                 | Description                              | Auth Required |
|--------|--------------------------|------------------------------------------|---------------|
| POST   | `/api/payment/create/`   | Create Stripe PaymentIntent for an order | Yes           |
| POST   | `/api/payment/verify/`   | Verify payment and update order status   | Yes           |

---

## Running with Docker

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running

### 1. Clone the repository
```bash
git clone https://github.com/PrashanthHosamani/Hoscart.git
cd Hoscart
```

### 2. Create your environment file
Create a `.env.docker` file in the project root. This file is listed in `.gitignore` and must never be committed.

```env
SECRET_KEY=your-django-secret-key
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=hoscart_db
DB_USER=hoscart_user
DB_PASSWORD=your-db-password
DB_HOST=db
DB_PORT=5432

STRIPE_SECRET_KEY=sk_test_your_stripe_key
```

### 3. Build and start all containers
```bash
docker compose --env-file .env.docker up --build
```

Docker will automatically:
- Build the Django application image
- Download PostgreSQL and Nginx images
- Run database migrations
- Collect static files
- Start all three containers

### 4. Access the API
```
http://localhost/api/
http://localhost/admin/
```

### 5. Stop all containers
```bash
docker compose down
```

---

## Local Development (Without Docker)

### Prerequisites
- Python 3.13+
- PostgreSQL installed locally

### 1. Clone and set up virtual environment
```bash
git clone https://github.com/PrashanthHosamani/Hoscart.git
cd Hoscart
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
```bash
export SECRET_KEY="your-secret-key"
export DEBUG="True"
export DB_NAME="hoscart_db"
export DB_USER="postgres"
export DB_PASSWORD="your-password"
export DB_HOST="localhost"
export DB_PORT="5432"
export STRIPE_SECRET_KEY="sk_test_..."
```

### 4. Run migrations and start the development server
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## AWS EC2 Deployment

The application is deployed on **AWS EC2 (t2.micro)** using the Free Tier.

### Deployment Stack
- OS: Ubuntu 24.04 LTS
- Web Server: Nginx (port 80) forwarding to Gunicorn (port 8000)
- Database: PostgreSQL running inside Docker
- Orchestration: Docker Compose

### Deployment Steps (Summary)
1. Launch EC2 `t2.micro` instance with Ubuntu (Free Tier)
2. Configure Security Group to open ports 22 (SSH) and 80 (HTTP)
3. SSH into the EC2 instance
4. Install Docker and Docker Compose on the instance
5. Clone the GitHub repository
6. Create `.env.docker` on the server with production credentials
7. Run `docker compose --env-file .env.docker up -d --build`

---

## Security Notes

- `SECRET_KEY`, database credentials, and Stripe API keys are never committed to GitHub
- All secrets are managed via `.env.docker`, which is listed in `.gitignore`
- `DEBUG=False` is enforced in production
- JWT access tokens expire in **20 minutes**; refresh tokens last **30 days**
- All API endpoints require authentication by default

---

## Future Improvements

- Wishlist system
- Product reviews and ratings
- Email notifications for order and payment confirmation
- Redis caching for product listings
- Celery for background task processing
- SSL/HTTPS with Let's Encrypt

---

## What I Learned

Through Hoscart, I gained hands-on experience with:

- Django REST Framework and advanced serializer design patterns
- JWT authentication and token-based security
- Relational database modeling with PostgreSQL
- Database transactions and data integrity patterns
- Stripe payment gateway integration
- Docker containerization with Dockerfile and Docker Compose
- Nginx reverse proxy configuration
- Gunicorn as a production WSGI server
- AWS EC2 provisioning and deployment
- Production-grade Django settings and environment variable management
- Git and GitHub version control workflows

---

## Final Note

Hoscart was built as a backend engineering project to understand how production-grade e-commerce systems are designed, secured, containerized, and deployed. The focus was not only on building features but on doing it correctly — with proper architecture, security practices, and production deployment standards.