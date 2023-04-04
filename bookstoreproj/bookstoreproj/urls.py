from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename="books")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('accounts/', include('accounts.urls')),
]