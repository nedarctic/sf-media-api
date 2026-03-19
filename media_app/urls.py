from django.urls import path
from .views import MediaUploadView, MediaListView

urlpatterns = [
    path('upload/', MediaUploadView.as_view(), name='upload'),
    path('files/', MediaListView.as_view(), name='files'),
]