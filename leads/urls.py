from django.urls import path
from .views import home_page

app_name = 'leads'
urlpatterns = [
    path('all/', home_page) # website.com/leads/all/ will go to the home_page view
]
