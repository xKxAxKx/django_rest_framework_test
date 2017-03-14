import os
import django_filters
from django.conf import settings
from rest_framework import viewsets, filters
from django.http.response import HttpResponse
from .models import User, Entry
from .serializer import UserSerializer, EntrySerializer

# 静的ファイルを返すview
def index(request):
    html = open(
        os.path.join(settings.STATICFILES_DIRS[0], "vue_grid.html")).read()
    return HttpResponse(html)

def entry(request):
    html = open(
        os.path.join(settings.STATICFILES_DIRS[0], "index.html")).read()
    return HttpResponse(html)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
