from django.urls import path, include
from rest_framework.routers import DefaultRouter
from home.views import Todoset
from . import views
# Setup the URLs and include login URLs for the browsable API.
from .views import index

router = DefaultRouter()

router.register('todo',Todoset)
urlpatterns = [
    path(r'', include(router.urls))
]
