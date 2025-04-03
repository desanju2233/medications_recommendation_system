# Medication Recommendation System

## Introduction
The **Medication Recommendation System** is a web-based application designed to help users get medication recommendations based on their symptoms. It uses **Machine Learning (Random Forest model)** trained on medical data to provide accurate predictions. The project is built with **Django** for the backend, **Tailwind CSS** for styling, and is deployed on **Render**.
🔗 **Live Demo**: [Medication Recommendation System]([https://medication-recommendation.onrender.com/home](https://medications-recommendation-system.onrender.com/home)

## Features
- **User Input Form**: Users can enter symptoms to receive medication suggestions.
- **Machine Learning Integration**: A **Random Forest** model predicts the best medication.
- **Responsive UI**: Designed with **Tailwind CSS** for a modern and mobile-friendly interface.
- **API Support**: Provides endpoints for external integrations.
- **Secure & Scalable**: Optimized for deployment on **Render**.
- **Database Support**: Uses **SQLite** (default) and **PostgreSQL** for production.

---

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML, Tailwind CSS
- **Machine Learning**: Random Forest (Joblib)
- **Database**: SQLite (default), PostgreSQL (production)
- **Deployment**: Render

---

## Installation Guide

### Prerequisites
Ensure you have the following installed:
- **Python 3.9+**
- **pip**
- **Git**
- **Virtual Environment** (optional but recommended)

### Step 1: Clone the Repository
```sh
git clone https://github.com/your-username/medication-recommendation.git
cd medication-recommendation
```

### Step 2: Set Up Virtual Environment (Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Step 3: Install Dependencies
```sh
pip install -r requirements.txt
```

### Step 4: Apply Migrations
```sh
python manage.py migrate
```

### Step 5: Load Sample Data (Optional)
```sh
python manage.py loaddata sample_data.json
```

### Step 6: Collect Static Files
```sh
python manage.py collectstatic --noinput
```

### Step 7: Run the Project Locally
```sh
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## Machine Learning Model Details
- The **Random Forest** model is trained on medical datasets.
- The trained model is saved as `random_forest_model.joblib` and loaded in Django views for inference.
- Uses optimized hyperparameters for better accuracy.

---

## API Endpoints
The project provides API endpoints for external system integrations.

### Available Endpoints:
- **GET /api/recommendation?query=fever** → Returns recommended medications for the given query.
- **POST /api/predict** → Accepts JSON data of symptoms and returns medication suggestions.

---

## Deployment on Render

### Step 1: Install Gunicorn
```sh
pip install gunicorn
```

### Step 2: Create a `requirements.txt`
```sh
pip freeze > requirements.txt
```

### Step 3: Create a `Procfile`
Create a file named `Procfile` (without extension) and add the following:
```sh
web: gunicorn your_project_name.wsgi
```

### Step 4: Push to GitHub
```sh
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin your-github-repo-url
git push -u origin main
```

### Step 5: Deploy on Render
1. Go to [Render](https://render.com/)
2. Click **New Web Service**
3. Connect your GitHub repository
4. Set **Build Command**:
   ```sh
   pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
   ```
5. Set **Start Command**:
   ```sh
   gunicorn your_project_name.wsgi
   ```
6. Set **Environment Variables**:
   - `DJANGO_SECRET_KEY`: A strong secret key
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `your_render_url`
   - `DATABASE_URL`: PostgreSQL URL if using Render DB
7. Click **Deploy**

Once deployed, visit the provided Render URL to access your app.

---

## Directory Structure
```sh
medication-recommendation/
│── medication_recommendation/   # Django project folder
│── templates/                    # HTML templates
│── static/                        # Static files (CSS, JS)
│── ml_model/                      # ML model directory
│   ├── random_forest_model.joblib
│── requirements.txt
│── manage.py
│── Procfile
│── render.yaml (optional)
│── README.md
```

---

## Contact
For any queries, reach out via:
- **Email**: desanju2233@gmail.com
