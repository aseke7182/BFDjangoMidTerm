from django.urls import path
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register('books', BookViewSet, basename='main')
router.register('journals', JournalViewSet, basename='main')

urlpatterns = [

]

urlpatterns += router.urls
