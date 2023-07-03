from django.urls import path
from Nj_contacts import views

urlpatterns = [
    path('', views.home, name=''),

    path('display_Contacts', views.display_contacts, name='display_Contacts'),

    path('submit_Contacts', views.show_Contact_Form, name='submit_Contacts'),

    path('display_School_Details/<int:pk>', views.school_details, name='display_School_Details'),

    path('update_school_record/<int:pk>', views.update_school_record, name='update_school_record'),

    path('delete_school_record/<int:pk>', views.delete_school_record, name='delete_school_record'),

    path('privacy_policy', views.privacy_policy, name='privacy_policy'),

    path('export_data_as_excel', views.export_data_as_excel, name='export_data_as_excel'),

    
    # path('accounts/signup/', views.privacy_policy, )
]