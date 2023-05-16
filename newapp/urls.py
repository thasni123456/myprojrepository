from django.urls import path
from . import views
app_name="newapp"
urlpatterns=[
    path('newapp',views.newapp,name='new'),
    path('aboutus',views.aboutus,name='aboutus')
    ]