from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView
from .models import Image
from .forms import ImageUploadForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageSerializer

class ImageListView(ListView):
    model = Image
    template_name = 'image_list.html'
    context_object_name = 'images'
    ordering = ['-uploaded_at']
    paginate_by = 12

class ImageUploadView(View):
    def get(self, request):
        form = ImageUploadForm()
        return render(request, 'upload.html', {'form': form})

    def post(self, request):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            return redirect('image_detail', pk=image.id)
        return render(request, 'upload.html', {'form': form})

class ImageDetailView(View):
    def get(self, request, pk):
        try:
            image = Image.objects.get(pk=pk)
            return render(request, 'image_detail.html', {'image': image})
        except Image.DoesNotExist:
            return redirect('upload')

class ImageUploadAPI(APIView):
    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.save()
            return Response({
                'id': image.id,
                'url': request.build_absolute_uri(image.image.url)
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)