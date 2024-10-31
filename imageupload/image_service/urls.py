from django.urls import path
from .views import ImageUploadView, ImageDetailView, ImageUploadAPI, ImageListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ImageListView.as_view(), name='image_list'),
    path('upload/', ImageUploadView.as_view(), name='upload'),
    path('image/<uuid:pk>/', ImageDetailView.as_view(), name='image_detail'),
    path('api/upload/', ImageUploadAPI.as_view(), name='api_upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)