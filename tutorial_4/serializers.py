from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class UserSerializer(serializers.ModelSerializer):
    # reverse relationship to snippets owned by user needs to be
    # explicitly defined in order that serializer can serialize a user
    # with all related snippets listed by their pk
    snippets = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Snippet.objects.all()
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')


# serializer with ModelSerializer
class SnippetSerializer(serializers.ModelSerializer):
    # read only representation of snippet owner
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ('id', 'owner', 'title', 'code', 'linenos', 'language',
                  'style')
