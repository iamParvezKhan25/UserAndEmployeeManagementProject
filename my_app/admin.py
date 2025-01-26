from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import User, Employee
from django.contrib import messages


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'date_joined')
    exclude = ["groups", "user_permissions", "is_staff", "last_login"]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'salary', 'manager', 'created_at')
    list_filter = ('position', 'created_at')
    search_fields = ('user__username', 'position')

    def delete_queryset(self, request, queryset):
        """
        Prevent bulk deletion of managers with subordinates.
        Suppress success messages when an error message is shown.
        """
        managers_with_subordinates = []
        deletable_employees = []

        # Separate managers with subordinates and deletable employees
        for obj in queryset:
            if obj.subordinates.exists():
                managers_with_subordinates.append(obj)
            else:
                deletable_employees.append(obj)

        if managers_with_subordinates:
            # Clear all existing messages, including the default success message
            list(messages.get_messages(request))

            # Add a custom error message
            messages.error(
                request,
                f"The following employees cannot be deleted because they have subordinates: "
                f"{', '.join(str(manager) for manager in managers_with_subordinates)}"
            )

        if deletable_employees:
            # Allow deletion for employees without subordinates
            queryset.filter(id__in=[obj.id for obj in deletable_employees]).delete()

            # Add a success message for successfully deleted employees
            messages.success(
                request,
                f"Successfully deleted {len(deletable_employees)} employees without subordinates."
            )

