from django.urls import path
from . import views
app_name = 'smp'
urlpatterns = [
    path('',views.home,name='predict_marks'),
]