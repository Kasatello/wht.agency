from rest_framework import viewsets

from team.models import Team
from team.serializers import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.select_related("member").all()
    serializer_class = TeamSerializer
