from django.shortcuts import render
from .models import photo


def image_list(request):
    images = photo.objects.all()
    return render(request, 'gallery/index.html', {'images': images})
