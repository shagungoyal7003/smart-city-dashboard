# 🚀 Smart City Open Data Aggregation Portal

A scalable web-based platform built using Django that collects, stores, and visualizes real-time urban data such as weather, air quality, and traffic.

---

## 📌 Features

- 🌦️ Real-time Weather Data using API
- 🌫️ Air Quality Monitoring (AQI)
- 🚗 Traffic Data Management (Mock Data)
- 📊 Interactive Dashboard (Table + Charts)
- 🔐 Admin Panel for Data Management
- 🗄️ Structured Database using Django ORM

---

## 🛠️ Tech Stack

- Backend: Django (Python)
- Database: SQLite
- Frontend: HTML, Bootstrap
- APIs: OpenWeather API
- Tools: Git, GitHub

---

## 📂 Project Structure
smartcity/
│
├── dashboard/
│ ├── models.py
│ ├── views.py
│ ├── utils.py
│ ├── urls.py
│
├── templates/
│ └── dashboard.html
│
├── static/
├── db.sqlite3
├── manage.py

---

## ⚙️ Installation & Setup

### 1. Clone Repository
git clone https://github.com/asus/smart-city-dashboard.git
cd smart-city-dashboard

### 2. Install Dependencies
pip install django djangorestframework requests

### 3. Run Migrations
python manage.py makemigrations
python manage.py migrate

### 4. Run Server
python manage.py runserver

## 🔑 API Setup
- Get API key from: https://openweathermap.org/
- Add it in `dashboard/utils.py`:
api_key = "dd40ad36972edf2b8f24cd1b610ff92b"

## 🚀 Future Enhancements

- 📊 Advanced Data Visualization (Charts)
- 🗺️ Map Integration (Leaflet)
- 🔐 User Authentication System
- ☁️ Cloud Deployment (AWS / Render)
- 🤖 AI-based Predictions

---

## 💡 Learning Outcomes

- Django Framework
- API Integration
- Database Design
- Full Stack Development Basics

## 📬 Contact

Shagun Goyal  
LinkedIn: https://www.linkedin.com/in/shagungoyal25/
---

⭐ If you like this project, give it a star!





