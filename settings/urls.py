from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from games.views import GameViewSet, GameFindViewSet


router = DefaultRouter()
router.register(r'game', GameViewSet)
router.register(r'games_find', GameFindViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls), name='game'),
]
