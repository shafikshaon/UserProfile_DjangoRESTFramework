from django.conf.urls import url
from . import views
from django.urls import include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('user', views.UserViewSet)  # if viewset is model viewset then base_name is not required
router.register('login', views.LoginViewSet, base_name='login')


urlpatterns = [
    url('hello/', views.HelloAPIView.as_view()),
    url('', include(router.urls)),
]
