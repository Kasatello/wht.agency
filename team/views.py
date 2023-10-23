from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from team.models import Team
from team.serializers import TeamSerializer

from django.shortcuts import get_object_or_404

from user.models import User


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.prefetch_related("members").all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAdminUser]

    @action(
        detail=True,
        methods=["POST"]
    )
    def add_member(self, request, pk=None):
        team = self.get_object_or_404(Team, pk=pk)
        user_id = request.data.get("user_id")
        user = get_object_or_404(User, pk=user_id)
        team.members.add(user)

        return Response(
            {"message": "Member added to the team"},
            status=status.HTTP_201_CREATED
        )
