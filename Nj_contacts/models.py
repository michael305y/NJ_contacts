from django.db import models
from django.core.validators import RegexValidator

SCHOOL_TYPE_CHOICES = (
            ('PUBLIC', 'PUBLIC'),
            ('PRIVATE', 'PRIVATE'),
        )

# Create your models here.
class Contact(models.Model):
    school_code = models.IntegerField()
    school_name = models.CharField(max_length=200)
    school_head = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=10, unique=True, validators=[RegexValidator(
                                                                                           regex=r"^0\d{9}$", 
                                                                                           message='Phone number should have 10 digits and start with 0 e.g. 0xxxxxxxxx', 
                                                                                           code='invalid_phone_number'
                                                                                        )], )
    
    
    type_of_school = models.CharField(max_length=20, choices=SCHOOL_TYPE_CHOICES)

    # school_category = models.Choices()

    email = models.EmailField()

    Location = models.CharField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.school_name


