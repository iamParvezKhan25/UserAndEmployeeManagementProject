from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.models import User
from .models import Employee, User
from .forms import UserForm, EmployeeForm, EmployeeUpdateForm
from django.contrib import messages


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


def user_detail(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'user_detail.html', {'user': user})


#
# def employee_detail(request, id):
#     employee = get_object_or_404(Employee, id=id)
#     return render(request, 'employee_detail.html', {'employee': employee})

def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        form = EmployeeUpdateForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee details updated successfully.')
            return redirect('employee_detail', id=id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = EmployeeUpdateForm(instance=employee)

    return render(request, 'employee_detail.html', {'employee': employee, 'form': form})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})


# View to delete an employee
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    # Check if the employee has subordinates before deleting
    if employee.subordinates.exists():
        messages.error(request, "This employee cannot be deleted because they have subordinates.")
        return redirect('employee_detail', id=id)

    # Delete the employee
    employee.delete()
    messages.success(request, "Employee deleted successfully.")
    return redirect('employee_list')  # Redirect to employee list or dashboard


# View to delete a user
def delete_user(request, id):
    user = get_object_or_404(User, id=id)

    # Check if the user is associated with an employee before deleting
    try:
        employee = Employee.objects.get(user=user)
        if employee.subordinates.exists():
            messages.error(request, "This user cannot be deleted because they have subordinates.")
            return redirect('user_detail', id=user.id)
    except Employee.DoesNotExist:
        pass  # Proceed if no Employee exists for the user

    # Delete the user
    user.delete()
    messages.success(request, "User deleted successfully.")
    return redirect('user_list')  # Redirect to user list or dashboard
