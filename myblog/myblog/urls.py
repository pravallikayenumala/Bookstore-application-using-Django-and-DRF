from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from bookstore.views import BookViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
