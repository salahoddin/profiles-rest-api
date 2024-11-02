from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet) # no need to pass base_name because this has a queryset
urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
    path('', include(router.urls)),
]