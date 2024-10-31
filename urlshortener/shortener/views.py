from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.http import Http404
from .models import URL
from .forms import URLForm

def create_short_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save()
            return render(request, 'shortener/success.html', {'url': url})
    else:
        form = URLForm()
    return render(request, 'shortener/create.html', {'form': form})

def redirect_to_original(request, short_url):
    try:
        url = get_object_or_404(URL, short_url=short_url)
        return redirect(url.original_url)
    except Http404:
        return render(request, 'shortener/not_found.html', status=404)

class URLListView(ListView):
    model = URL
    template_name = 'shortener/list.html'
    context_object_name = 'urls'
    ordering = ['-created_at']