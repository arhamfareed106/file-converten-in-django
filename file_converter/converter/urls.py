from django.urls import path
from . import views

urlpatterns = [
    path('', views.convert_file_view, name='convert_file'),  # Define the root URL
    path('convert/', views.convert_file, name='convert_file_logic'),  # Your conversion logic
    path('download/<str:file_name>/', views.download_file_view, name='download_file'),  # Download link
]
