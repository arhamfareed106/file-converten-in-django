from django.urls import path
from . import views

urlpatterns = [
    path('', views.convert_file_view, name='convert_file'),  # Main file conversion view
    path('download/<str:file_name>/', views.download_file_view, name='download_file'),  # Download link
]
 