from django.shortcuts import render, get_object_or_404 # Add get_object_or_404 to your imports
from .models import Chronicle

def home(request):
# Get only the single most recent post    
    latest_post = Chronicle.objects.order_by('-created_at').first()
    return render(request, 'core/home.html', {'post': latest_post})

# New function for the single post page
def chronicle_detail(request, pk):
    post = get_object_or_404(Chronicle, pk=pk)
    return render(request, 'core/chronicle_detail.html', {'post': post})

def chronicles_archive(request):
    # Get all posts for the archive
    all_posts = Chronicle.objects.all().order_by('-created_at')
    return render(request, 'core/chronicles_archive.html', {'posts': all_posts})

# the static pages
def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def machines(request):
    return render(request, 'core/machines.html')