from django.urls import path
from .views import MediaUploadView, MediaListView, MediaDownloadView

urlpatterns = [
    path('upload/', MediaUploadView.as_view(), name='upload'),
    path('files/', MediaListView.as_view(), name='files'),
    path('files/<int:pk>/download/', MediaDownloadView.as_view(), name='media-download'),
]