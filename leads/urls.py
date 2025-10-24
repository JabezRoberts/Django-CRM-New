from django.urls import path
from .views import lead_detail, lead_list

app_name = 'leads'
urlpatterns = [
    path('', lead_list), # website.com/leads/all/ will go to the home_page view
    path('<int:pk>/', lead_detail)
]
