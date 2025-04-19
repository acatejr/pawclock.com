from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Owner(BaseModel):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    phone = models.CharField(max_length=15, null=False, blank=False)

    class Meta:
        verbose_name = "Owner"
        verbose_name_plural = "Owners"

    def __str__(self):
        return self.first_name + " " + self.last_name

PET_TYPE_CHOICES = [
    ("dog", "Dog"),
    ("cat", "Cat"),
    ("other", "Other"),
]

class Pet(BaseModel):
    name = models.CharField(max_length=100)
    owners = models.ManyToManyField(Owner, related_name="pets")
    pet_type = models.CharField(
        max_length=10, choices=PET_TYPE_CHOICES, default="dog"
    )

    class Meta:
        verbose_name = "Pet"
        verbose_name_plural = "Pets"

    def __str__(self):
        return self.name


class DayCareSession(BaseModel):
    pet = models.ForeignKey(
        Pet, on_delete=models.CASCADE, related_name="day_care_sessions"
    )
    check_in_owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
        related_name="check_in_sessions",
        blank=True,
        null=True,
    )
    check_in_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="check_in_users",
        blank=True,
        null=True,
    )
    check_out_owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
        related_name="check_out_sessions",
        blank=True,
        null=True,
    )
    check_out_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="check_out_users",
        blank=True,
        null=True,
    )
    # check_in = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    check_in = models.DateTimeField(blank=True, null=True)
    check_out = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Day Care Session"
        verbose_name_plural = "Day Care Sessions"

    def __str__(self):
        return f"{self.pet.name} - {self.check_in} to {self.check_out}"

    def session_duration(self):
        if self.check_in and self.check_out:
            duration = round((self.check_out - self.check_in).total_seconds() / 3600, 2)
            return duration

        return None
