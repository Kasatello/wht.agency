from rest_framework import serializers

from team.models import Team
from user.models import User


class TeamSerializer(serializers.ModelSerializer):
    class TeamSerializer(serializers.ModelSerializer):
        members = serializers.PrimaryKeyRelatedField(
            queryset=User.objects.all(), many=True
        )

    class Meta:
        model = Team
        fields = ("name", "members")

    def validate_members(self, members):
        instance = self.instance

        for user in members:
            teams = Team.objects.filter(members=user)
            if instance:
                teams = teams.exclude(pk=instance.pk)
            if teams.exists():
                raise serializers.ValidationError(
                    "This person is already in another team."
                )
        return members

    def get_member_name(self, user_id):
        user = User.objects.get(id=user_id)
        return f"{user.first_name} {user.last_name}"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['members'] = [
            self.get_member_name(member)
            for member in representation['members']
        ]
        return representation
