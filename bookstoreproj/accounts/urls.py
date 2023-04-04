from django.urls import path

from accounts.views import BookstoreprojListView, LoginView, Registrationview, Verifyview
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('register/', Registrationview.as_view()),
    path('verify/', Verifyview.as_view()),
    path('api/token/', LoginView.as_view()),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view()),
    path('api/bookstore-post/',BookstoreprojListView.as_view()),
]

