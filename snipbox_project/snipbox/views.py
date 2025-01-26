from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import SnippetSerializer


class SnippetCreateAPI(generics.CreateAPIView):
    """API to create a new snippet"""
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
