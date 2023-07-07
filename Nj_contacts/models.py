from django.db import models
from django.core.validators import RegexValidator

SCHOOL_TYPE_CHOICES = (
            ('PUBLIC', 'PUBLIC'),
            ('PRIVATE', 'PRIVATE'),
        )

SCHOOL_CATEGORY_CHOICES = (
            ('PRIMARY', 'PRIMARY'),
            ('SECONDARY', 'SECONDARY'),
        )

SCHOOL_LOCATION_CHOICES = (
            ('Babadogo', 'Babadogo'),
            ('Chokaa', 'Chokaa'),
            ('Dandora', 'Dandora'),
            ('Dandora phase 1', 'Dandora phase 1'),
            ('Dandora phase 2', 'Dandora phase 2'),
            ('Dandora Phase 3', 'Dandora phase 3'),
            ('Kamulu', 'Kamulu'),
            ('Kamulu Kipawa', 'Kamulu Kipawa'),
            ('Kariobangi', 'Kariobangi'),
            ('Kariobangi South', 'Kariobangi South'),
            ('Kayole', 'Kayole'),
            ('Kayole Junction', 'Kayole Junction'),
            ('Kayole North', 'Kayole North'),
            ('KCC', 'KCC'),        
            ('Kwa Maji', 'Kwa Maji'),
            ('Maili Saba', 'Maili Saba'),
            ('Mihango', 'Mihango'),
            ('Mowlem', 'Mowlem'),
            ('Njiru', 'Njiru'),
            ('Obama', 'Obama'),
            ('Ruai', 'Ruai'),
            ('Ruai Block 10', 'Ruai Block 10'),
            ('Saika', 'Saika'),
            ('Sewage', 'Sewage'),
            ('Silanga', 'Silanga'),
            ('Spring valley', 'Spring valley'),
            ('Umoja', 'Umoja'),
            ('Umoja 3', 'Umoja 3'),
            ('Utawala', 'Utawala'),
            ('Utawala githunguri', 'Utawala githunguri'),
            ('other', 'other'),
        )




# Create your models here.
class Contact(models.Model):
    # school_code = models.IntegerField()
        #  ^20409\d{3}$
    school_code = models.CharField(max_length=8, unique=True, validators=[RegexValidator(
                                                                            regex=r"^20409\d{3}$", 
                                                                            message='School code should have 8 digits', 
                                                                            code='invalid_school_code'
                                                                                )], )

    school_name = models.CharField(max_length=200)

    # school_head = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=10, unique=True, validators=[RegexValidator(
                                                                                           regex=r"^0\d{9}$", 
                                                                                           message='Phone number should have 10 digits and start with 0 e.g. 0xxxxxxxxx', 
                                                                                           code='invalid_phone_number'
                                                                                        )], )
    
    
    type_of_school = models.CharField(max_length=20, choices=SCHOOL_TYPE_CHOICES)

    school_category = models.CharField(max_length=20, choices=SCHOOL_CATEGORY_CHOICES)

    # email = models.EmailField()

    location = models.CharField(max_length=30, choices=SCHOOL_LOCATION_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)

    # capitalize names
    def clean(self):
        self.school_name = self.school_name.title()

        # self.school_head = self.school_head.title()

        self.Location = self.school_name.title()

    def __str__(self) -> str:
        return self.school_name


