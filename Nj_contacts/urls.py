from django.urls import path
from Nj_contacts import views

urlpatterns = [
    path('', views.home, name=''),

    path('display_Contacts', views.display_contacts, name='display_Contacts'),

    path('submit_Contacts', views.show_Contact_Form, name='submit_Contacts'),

    path('display_School_Details/<int:pk>', views.school_details, name='display_School_Details'),

    path('update_school_record/<int:pk>', views.update_school_record, name='update_school_record'),

    path('delete_school_record/<int:pk>', views.delete_school_record, name='delete_school_record'),


    # ============ collection points view ===============================================================
    path('display_kcpe_collection_points', views.display_kcpe_collection_points, name='display_kcpe_collection_points'), # to display KCPE collection points

    path('show_KCPE_collection_form', views.show_KCPE_collection_form, name='show_KCPE_collection_form'),

    path('update_KCPE_collection_point/<int:pk>', views.update_KCPE_collection_point, name='update_KCPE_collection_point'),

    path('display_detailed_KCPE_collection_point/<int:pk>', views.display_detailed_KCPE_collection_point, name='display_detailed_KCPE_collection_point'),

    path('delete_KCPE_collection_point/<int:pk>', views.delete_KCPE_collection_point, name='delete_KCPE_collection_point'),



    # ==========================#=======================================
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),

    path('export_data_as_excel', views.export_data_as_excel, name='export_data_as_excel'),
    

    # ========= htmx url search ========================================================================
    path('search/', views.search_school, name='search_school')

    
    # path('accounts/signup/', views.privacy_policy, )
]