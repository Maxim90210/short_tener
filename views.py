import string
import random
from django.shortcuts import render, redirect
from .forms import URLForm
from .storage import save_url, get_url

def generate_short_id(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def index(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            short_id = generate_short_id()
            save_url(short_id, original_url)
            return render(request, 'shortener/success.html', {'short_id': short_id})
    else:
        form = URLForm()

    return render(request, 'shortener/index.html', {'form': form})

def redirect_url(request, short_id):
    original_url = get_url(short_id)
    if original_url:
        return redirect(original_url)
    else:
        return render(request, 'shortener/404.html', status=404)
