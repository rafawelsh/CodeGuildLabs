from django.urls import path
from . import views

app_name = 'libraryapp' # for namespacing
urlpatterns = [
    path('', views.index, name='index')
]
