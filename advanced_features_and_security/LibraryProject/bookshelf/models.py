from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# -----------------------------
# Custom User Manager
# -----------------------------
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username must be set")
        if not email:
            raise ValueError("The Email must be set")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(username, email, password, **extra_fields)


# -----------------------------
# Custom User Model
# -----------------------------
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(
        upload_to="profile_photos/",
        null=True,
        blank=True
    )

    objects = CustomUserManager()

    def __str__(self):
        return self.username


# -----------------------------
# Book Model
# -----------------------------
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def save(self, *args, **kwargs):
        if not self.id:
            max_id = Book.objects.aggregate(models.Max('id'))['id__max']
            self.id = max_id + 1 if max_id else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"id={self.id} "
            f"title={self.title} "
            f"author={self.author} "
            f"published_date={self.published_date}"
        )
    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]