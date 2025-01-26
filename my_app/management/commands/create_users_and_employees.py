import random
from django.core.management.base import BaseCommand
from faker import Faker
from my_app.models import User, Employee


class Command(BaseCommand):
    help = "Generate 25 users and employees"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create 25 users and corresponding employees
        for _ in range(25):
            username = fake.user_name()
            email = fake.unique.email()

            # Create the user
            user = User.objects.create_user(
                username=username,
                email=email,
                password="password123",  # Default password for all users
            )

            # Assign a random position and salary
            position = random.choice(['Manager', 'Developer', 'Designer', 'Analyst'])
            salary = random.randint(30000, 120000)

            # Assign a random manager (excluding the current employee)
            existing_employees = Employee.objects.exclude(user=user)
            manager = random.choice(existing_employees) if existing_employees.exists() else None

            # Create the employee
            Employee.objects.create(
                user=user,
                position=position,
                salary=salary,
                manager=manager,
            )

        self.stdout.write(self.style.SUCCESS("Successfully created 25 users and employees"))
