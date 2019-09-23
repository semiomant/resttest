from django.urls import include, path
from rest_framework.authtoken import views as authviews
from rest_framework import routers

from example import views

router = routers.DefaultRouter()
router.register(r'examples', views.ExampleViewSet)
router.register(r'ex2', views.Example2ViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('gimme-token/', authviews.obtain_auth_token),
]
