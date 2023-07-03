from django.contrib import admin
from . models import Contact

# creating an admin class to show all the sepcified fields on the admin page
class My_admin(admin.ModelAdmin):
    # the list needs to be explicitly defined with the appropriate fields
    # generalization with the __all__ special method wont work
    list_display = ['school_code','school_name', 'type_of_school','created_at',]
    search_fields = ['school_code','school_name','created_at', 'type_of_school']
    list_per_page = 10
    
    
    

# Register your models here.
admin.site.register(Contact, My_admin)