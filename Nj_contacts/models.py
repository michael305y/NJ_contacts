from django.db import models

# Create your models here.
class Contact(models.Model):
    school_code = models.IntegerField()
    school_name = models.CharField(max_length=200)
    school_head = models.CharField(max_length=200)
    Mobile_number = models.IntegerField()
    Location = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.school_name


