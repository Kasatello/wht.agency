from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/", include("user.urls", namespace="user")),
    path("api/teams/", include("team.urls", namespace="team")),
    path("__debug__/", include("debug_toolbar.urls")),
]
