from django.urls import path, include

from rest_framework import routers

from team.views import TeamViewSet

router = routers.DefaultRouter()
router.register("teams", TeamViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "team"
