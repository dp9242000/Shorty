from django.shortcuts import render, redirect
from django.http import HttpResponse
import uuid
from .models import Url
import re

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    httpRegex = re.compile(r'(^https?://)')
    url = url_details.link
    if httpRegex.findall(url):
        return redirect(url)
    else:
        return redirect('https://'+url)


