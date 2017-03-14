from rest_framework import routers
from .views import UserViewSet, EntryViewSet
from django.conf.urls import url
from blog.views import index, entry


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'entries', EntryViewSet)

urlpatterns = [
    # blog/
    url(r'^$', index, name='index'),
    url(r'^entry/$', entry, name='entry'),
]
