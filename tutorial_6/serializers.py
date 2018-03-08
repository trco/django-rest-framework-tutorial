from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # reverse relationship to snippets owned by user needs to be
    # explicitly defined in order that serializer can serialize a user
    # with all related snippets listed by their pk
    snippets = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='snippet-detail',
        read_only=True
    )

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')


# serializer with ModelSerializer
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # read only representation of snippet owner
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight',
        format='html'
    )

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos',
                  'language', 'style')
