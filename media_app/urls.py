from django.urls import path
from .views import MediaUploadView, MediaListView, MediaDownloadView, LogoUploadView, LogoListView, LogoDownloadView

urlpatterns = [
    path('upload/', MediaUploadView.as_view(), name='upload'),
    path('files/', MediaListView.as_view(), name='files'),
    path('files/<int:pk>/download/', MediaDownloadView.as_view(), name='media-download'),
    
    path('logos/upload/', LogoUploadView.as_view()),
    path('logos/', LogoListView.as_view()),
    path('logos/<int:pk>/download/', LogoDownloadView.as_view()),
]