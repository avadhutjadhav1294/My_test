"""Library_assign_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_view, name="home"),
    path('active/', views.active_books, name="active_books"),
    path('inactive/', views.inactive_books, name="inactive_books"),
    path('update/<int:id>', views.home_view, name="update_book"), # here seperate url is given because at the time of starting the view id is not passed and it raises the error
    path('delete/<int:id>', views.hard_delete, name="hard_delete"),
    path('soft-delete/<int:id>', views.soft_delete, name="soft_delete"),
    path('restore/<int:id>', views.restore_book, name="restore_book"),
    path('export-csv/', views.export_csv, name="export_csv"),
    path('upload-csv/', views.upload_csv, name="upload_csv"),
    path('export-active/', views.export_active, name="export_active"),
    path('export-inactive/', views.export_inactive, name="export_inactive"),
    path('upload-text/', views.upload_text, name="upload_text"),
]
