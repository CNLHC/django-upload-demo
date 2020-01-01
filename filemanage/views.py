from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse
from .models import StaticObject
from django.core import serializers

class FileManageView(View):
    def get(self,request):
        return HttpResponse(serializers.serialize('json',StaticObject.objects.all()),content_type="application/json")

    def post(self,request):
        files = request.FILES.getlist('file')
        for f in files:
            StaticObject.objects.create(FileName=f.name,FileObj=f)
        return JsonResponse({'status':'ok'})


