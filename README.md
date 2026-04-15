# 🛒 Hoscart – Scalable E-commerce Backend API

Hoscart is a production-oriented e-commerce backend built using Django REST Framework.  
It is designed to simulate real-world backend systems by handling authentication, product management, cart workflows, order processing, and performance optimization.

The project focuses on building a **scalable, maintainable, and production-ready backend system**, not just basic CRUD APIs.

---

# 🎯 Project Vision

The goal of Hoscart is to build a backend system that reflects how real e-commerce platforms operate, including:

- structured API design
- database integrity and relationships
- performance optimization
- scalable architecture
- production-ready workflows

---

# 🚀 Features

## ✅ Core Features (Implemented)

### 🔐 Authentication
- User registration
- Login using JWT
- Secure API access

### 📦 Product Management
- Product CRUD operations
- Filtering and search
- Pagination support

### 🛒 Cart System
- Add items to cart
- Update quantity
- Remove items
- Stock validation
- Prevent duplicate cart entries

### 📦 Order System
- Create order from cart
- Store order item snapshots
- Clear cart after checkout
- Order history tracking

### ⚡ Performance Optimization
- Query optimization using `select_related`
- Caching mechanism (LRU / Redis)
- Pagination for large datasets

---

## 🔄 Upcoming Features (Planned)

### ❤️ Wishlist
- Add/remove products
- User-specific wishlist

### ⭐ Reviews & Ratings
- Product reviews
- Rating system

### 💳 Payments
- Stripe integration
- Payment status handling

### 📧 Email System
- Order confirmation emails
- Notifications

### 📊 Analytics (Future Scope)
- Sales tracking
- User activity insights

---

# 🏗️ Tech Stack

- **Backend:** Python, Django, Django REST Framework  
- **Database:** PostgreSQL  
- **Caching:** Redis / LRU Cache  
- **Authentication:** JWT  
- **Deployment:** AWS / Render  
- **Tools:** Postman, Git, GitHub  

---

# 🧠 System Architecture

---

# 📌 API Design

The system follows RESTful API principles.

---

## 🔐 Authentication APIs

| Method | Endpoint | Description |
|-------|--------|------------|
| POST | /api/register/ | Register user |
| POST | /api/login/ | Login user |
| POST | /api/token/refresh/ | Refresh JWT |

---

## 📦 Product APIs

| Method | Endpoint | Description |
|-------|--------|------------|
| GET | /api/products/ | List products |
| GET | /api/products/{id}/ | Product details |
| POST | /api/products/ | Create product |
| PUT | /api/products/{id}/ | Update product |
| DELETE | /api/products/{id}/ | Delete product |

Supports:
- Filtering
- Search
- Pagination

---

## 🛒 Cart APIs

| Method | Endpoint | Description |
|-------|--------|------------|
| GET | /api/cart/ | View cart |
| POST | /api/cart/add/ | Add item |
| PATCH | /api/cart/update/ | Update quantity |
| DELETE | /api/cart/remove/ | Remove item |

### Cart Logic

- If product exists → update quantity  
- If quantity > stock → reject  
- If quantity = 0 → remove item  

---

## 📦 Order APIs

| Method | Endpoint | Description |
|-------|--------|------------|
| POST | /api/orders/create/ | Create order |
| GET | /api/orders/ | Order history |

### Order Flow

---

# 🧠 Database Design

### Key Relationships

- User → Cart (One-to-One)
- Cart → CartItems (One-to-Many)
- Product → CartItems (Many-to-One)
- Order → OrderItems (One-to-Many)

---

## Key Concepts Used

- Normalization  
- Controlled denormalization (Order price snapshot)  
- Referential integrity  
- Constraints (unique_together)  

---

# ⚡ Performance Optimization

- Used `select_related` to avoid N+1 queries  
- Implemented caching for frequently accessed data  
- Pagination to handle large datasets  

---

# 🔒 Security

- JWT-based authentication  
- Protected endpoints  
- Input validation  
- User-specific data access  

---

# 🧪 Future Enhancements

- Transaction handling (`atomic`)  
- Rate limiting  
- Logging & monitoring  
- CI/CD pipelines  
- Test coverage  

---

# ⚙️ Setup Instructions

## 1. Clone Repository
```bash
git clone https://github.com/your-username/hoscart.git
cd hoscart

2. Create Virtual Environment
python -m venv env
source env/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url

5. Run Migrations
python manage.py makemigrations
python manage.py migrate

6. Run Server
python manage.py runserver
