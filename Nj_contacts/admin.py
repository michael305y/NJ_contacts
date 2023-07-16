from django.contrib import admin
from . models import Contact, KCPE_collection_point, Kcse_collection_point, Kepsea_collection_point

# creating an admin class to show all the sepcified fields on the admin page
class My_admin(admin.ModelAdmin):
    # the list needs to be explicitly defined with the appropriate fields
    # generalization with the __all__ special method wont work
    list_display = ['school_code','school_name', 'type_of_school', 'school_category', 'created_at',]
    search_fields = ['school_code','school_name', 'created_at', 'type_of_school']
    list_per_page = 10

    

# # creating an admin class to show all the sepcified fields on the admin page for KCPE COLLECTION POINTS
# class My_admin_2(admin.ModelAdmin):
#     # the list needs to be explicitly defined with the appropriate fields
#     # generalization with the __all__ special method wont work
#     list_display = ['school_code','school_name', 'type_of_school', 'school_category', 'created_at',]
#     search_fields = ['school_code','school_name', 'created_at', 'type_of_school']
#     list_per_page = 10
    
    
    

# Register your models here.
admin.site.register(Contact, My_admin)
admin.site.register(KCPE_collection_point)

admin.site.register(Kepsea_collection_point)

admin.site.register(Kcse_collection_point)