# from django.db.models.signals import pre_delete, post_save
# from django.dispatch import receiver
# from django.core.exceptions import ValidationError
# from .models import User, Employee
#
#
# @receiver(post_save, sender=User)
# def create_employee_profile(sender, instance, created, **kwargs):
#     if created:
#         Employee.objects.create(user=instance)
#
#
# @receiver(pre_delete, sender=User)
# def delete_employee_profile(sender, instance, **kwargs):
#     # Ensure the Employee is deleted when the User is deleted
#     try:
#         instance.employee.delete()
#     except Employee.DoesNotExist:
#         pass

from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import User, Employee


@receiver(post_delete, sender=User)
def delete_associated_employee(sender, instance, **kwargs):
    """
    Deletes the associated Employee when a User is deleted.
    """
    try:
        # Check if the User has an associated Employee
        employee = Employee.objects.get(user=instance)
        employee.delete()
    except Employee.DoesNotExist:
        # No associated Employee exists; do nothing
        pass
