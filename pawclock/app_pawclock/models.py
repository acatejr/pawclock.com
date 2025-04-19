from django.db import models

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


class Pet(BaseModel):
    name = models.CharField(max_length=100)
    owners = models.ManyToManyField(Owner, related_name='pets')
    # age = models.IntegerField()
    # species = models.CharField(max_length=100)
    # breed = models.CharField(max_length=100)
    # weight = models.FloatField()
    # owner_name = models.CharField(max_length=100)
    # owner_contact = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Pet"
        verbose_name_plural = "Pets"

    def __str__(self):
        return self.name
