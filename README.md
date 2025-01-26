# Django User and Employee Management Project

## Project Setup Instructions

Follow the steps below to set up and run the project on your local machine.

### Prerequisites

Make sure you have the following installed on your system:
- Python 3.8+
- pip (Python package manager)
- Virtualenv (recommended)
- Git

---

## Installation Guide

### Step 1: Clone the Repository
```bash
git clone https://github.com/iamParvezKhan25/UserAndEmployeeManagementProject.git
cd UserAndEmployeeManagementProject
```

### Step 2: Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate    # For Windows
```

### Step 3: Install Dependencies
Install the required Python packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Step 4: Apply Migrations
Run the following commands to set up the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Generate Fake Data (Optional)
To quickly create 25 users and employees, use the following command:
```bash
python manage.py shell
```
Then, run the following script inside the Django shell:
```python
from faker import Faker
from my_app.models import User, Employee

faker = Faker()
for _ in range(25):
    user = User.objects.create_user(
        username=faker.user_name(),
        email=faker.email(),
        password="password123"
    )
    Employee.objects.create(
        user=user,
        position=faker.job(),
        salary=faker.random_int(min=30000, max=120000),
        manager=None  # Adjust manager assignment logic if needed
    )
```
Exit the shell with `exit()`.

### Step 6: Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```
Access the application in your browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Project Features

### User Management
- View a list of all users
- Add, update, and delete users
- Detailed user view

### Employee Management
- View a list of all employees
- Add, update, and delete employees
- Assign or update managers for employees

### Admin Dashboard
- Custom admin panel for managing users and employees
- Prevent deletion of managers with subordinates

---

## Key Commands

### Create Superuser
To create an admin user:
```bash
python manage.py createsuperuser
```

### Access Admin Panel
Access the admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

---

## Additional Notes

### Folder Structure
- `my_app/`: Contains the core app files (models, views, forms, templates, etc.)
- `templates/`: Contains HTML templates
- `static/`: Contains CSS and JS files
- `requirements.txt`: Lists all dependencies

---

## Troubleshooting

If you encounter any issues, check the following:
1. Ensure all dependencies are installed correctly.
2. Ensure the database migrations are applied.
3. Check error logs in the terminal for debugging.

Feel free to raise issues or contribute to this repository!
