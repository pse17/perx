from django.urls import path
from .api import FileView

urlpatterns = [
    path('upload/', FileView.as_view(), name='file-upload'),
]