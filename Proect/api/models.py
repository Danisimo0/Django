from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings

# Model for user role
class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Custom model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def save(self, *args, **kwargs):
        if self.pk is None:  # Check if this is a new user
            if not self.role:
                self.role = Role.objects.get(name='User')  # Default role
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.email})"

# Model for teacher
class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teacher_profile')
    subject = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.subject}"

# Model for student
class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile')
    date_of_birth = models.DateField()
    grade = models.CharField(max_length=10, default='Unknown')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    teachers = models.ManyToManyField(Teacher, related_name='students', blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - Grade: {self.grade}"

class StripeCustomer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.stripeCustomerId}"

class MonthlyOutput(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    output_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.output_count}"
