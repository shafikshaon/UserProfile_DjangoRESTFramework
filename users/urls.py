from django.conf.urls import url
from . import views
from django.urls import include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.ProfileViewSet)


urlpatterns = [
    url('hello/', views.HelloAPIView.as_view()),
    url('', include(router.urls)),
]
