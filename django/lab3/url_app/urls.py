from django.urls import path
from . import views

app_name = 'url_app' # for namespacing

urlpatterns = [
    path('', views.index, name='index'),
    path('shorten', views.shorten, name='shorten'),
    path('<code>', views.redirector, name='redirect')
    # path('url_app/success', views.success, name='success')
]
