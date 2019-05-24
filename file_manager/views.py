from django.shortcuts import render
from django.http import Http404

# Create your views here.


def upload(request):
    return render(request, 'file_manager/upload.html')


def result(request):
    if request.method == 'POST':
        upload_file = request.FILES['document']
        del upload_file
    raise Http404("Upload file are delete")
