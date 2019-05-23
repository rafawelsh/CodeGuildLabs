from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Url_short
import random
import string

def index(request):
    ushort = Url_short.objects.all()
    return render(request, 'url_app/index.html')

def shorten(request):
    if request.method == 'POST':
        long_url = request.POST['url']
        short = code_generator()
        url = Url_short(long_url=long_url, code=short)
        url.save()
    return render(request, 'url_app/success.html', {'short': short, 'long_url':url})

def redirector(request, code):
    url = get_object_or_404(Url_short, code=code)
    long = url.long_url
    if not long.startswith('http'):
        long = 'http://' + long
    return redirect(long)

def code_generator(size=6):
    chars=string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

#
# def redirect(request):
