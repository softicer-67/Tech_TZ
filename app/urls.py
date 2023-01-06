from django.urls import include, path
from rest_framework import routers

from app.views import OrderFormViewSet, index, answer

router = routers.DefaultRouter()
router.register(r'user', OrderFormViewSet)


urlpatterns = [
    path('', index, name='index'),
    path('user/', OrderFormViewSet.as_view({'get': 'list'})),
    path('<slug:user>/', answer, name='answer'),
    path('', include(router.urls)),
]


