from django.shortcuts import render, redirect
from django.http import HttpResponse
import uuid
from .models import Url
import re

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        # url is the url as submitted by the user
        url = request.POST['link']
        # regex object to ensure the provided url is prefixed by https://
        httpRegex = re.compile(r'(^https?://)')
        # check if the url is prefixed with https://
        if not httpRegex.findall(url):
            url = 'https://' + url
        # generate uuid to store with the provided url
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=url, uuid=uid)
        new_url.save()
        return HttpResponse(uid)


# pk = uuid, get the url using the uuid and then redirect
def go(request, pk):
    return redirect(str(Url.objects.get(uuid=pk)))



