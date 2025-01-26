from rest_framework import serializers
from .models import Snippet, Tag


class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tag model"""

    class Meta:
        model = Tag
        fields = ['id', 'title']


class SnippetSerializer(serializers.ModelSerializer):
    """Serializer for Snippet model"""
    tags = serializers.ListField(child=serializers.CharField(), write_only=True)
    tag_objects = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'note', 'created_at', 'updated_at', 'tags', 'tag_objects']

    def get_tag_objects(self, obj):
        """Return tag titles instead of IDs."""
        return [tag.title for tag in obj.tags.all()]

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        snippet = Snippet.objects.create(**validated_data)

        for tag_title in tags_data:
            tag, created = Tag.objects.get_or_create(title=tag_title)
            snippet.tags.add(tag)

        return snippet
