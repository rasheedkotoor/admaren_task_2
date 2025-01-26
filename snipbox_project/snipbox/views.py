from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import SnippetSerializer, TagSerializer
from .models import Snippet, Tag


class SnippetOverviewAPI(generics.ListAPIView):
    """API to list all snippets with total count (only for the owner)"""
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Snippet.objects.filter(created_by=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        response_data = {
            "total_snippets": queryset.count(),
            "snippets": self.get_serializer(queryset, many=True).data
        }
        return Response(response_data)


class SnippetCreateAPI(generics.CreateAPIView):
    """API to create a new snippet"""
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class SnippetDetailAPI(generics.RetrieveAPIView):
    """API to retrieve snippet details (only for the owner)"""
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Snippet.objects.filter(created_by=self.request.user)


class TagListAPIView(generics.ListAPIView):
    """
    API to list all tags.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


class TagDetailAPIView(generics.RetrieveAPIView):
    """
    API to retrieve snippets linked to a specific tag.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]
