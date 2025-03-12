# Project Setup

This project sets up a **Django backend** running inside **Docker**, with **PostgreSQL** as the database and support for **Vue 3 + Quasar** in the future.

---

## 🚀 **Getting Started**

### **1. Clone or Create the Project Directory**

```sh
mkdir docker-django && cd docker-django
```

### **2. Create the Necessary Files**

Ensure you have the following structure:

```
docker-django/
├── Dockerfile
├── docker-compose.yml
├── backend/
│   ├── project/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── __init__.py
│   ├── manage.py
│   ├── requirements.txt
└── frontend/  # Placeholder for Vue 3 + Quasar (future integration)
```

---

## 🛠 **Setting Up the Django Project in Docker**

### **1. Build and Start the Docker Containers**

```sh
docker-compose up --build -d
```

This will:

- Build the Django container
- Start PostgreSQL
- Run Django on `http://localhost:8000`

### **2. Run Migrations**

Before using Django, apply migrations to set up the database:

```sh
docker-compose exec backend python manage.py migrate
```

### **3. Create a Superuser**

To access Django Admin, create a superuser:

```sh
docker-compose exec backend python manage.py createsuperuser
```

Enter the required details (**username, email, password**).

### **4. Access Django Admin**

- Open: `http://localhost:8000/admin/`
- Login with the **superuser credentials** created in the previous step.

---

## 🛠 **Troubleshooting**

### **1. "ModuleNotFoundError: No module named 'dj_database_url'"**

🔹 **Cause:** Missing Python dependency inside the container.

✅ **Fix:** Ensure `dj-database-url` is in `backend/requirements.txt`:

```txt
Django>=4.2
gunicorn
psycopg2-binary
djangorestframework
django-cors-headers
dj-database-url
```

Then, rebuild the container:

```sh
docker-compose build
```

Restart everything:

```sh
docker-compose up --build
```

### **2. "relation 'auth_user' does not exist"**

🔹 **Cause:** Database migrations have not been applied.

✅ **Fix:** Run the following command:

```sh
docker-compose exec backend python manage.py migrate
```

Then, retry creating a superuser:

```sh
docker-compose exec backend python manage.py createsuperuser
```
