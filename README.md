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
