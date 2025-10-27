from django.contrib import admin
from django.urls import path
from library_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_phones),
]