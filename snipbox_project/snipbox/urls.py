from django.urls import path
from .views import SnippetCreateAPI, SnippetOverviewAPI, SnippetDetailAPI, SnippetUpdateAPI, SnippetDeleteAPI
from .views import TagListAPIView, TagDetailAPIView


urlpatterns = [
    path('snippets/', SnippetOverviewAPI.as_view(), name='snippet-overview'),
    path('snippets/create/', SnippetCreateAPI.as_view(), name='snippet-create'),
    path('snippets/<int:pk>/', SnippetDetailAPI.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/update/', SnippetUpdateAPI.as_view(), name='snippet-update'),
    path('snippets/<int:pk>/delete/', SnippetDeleteAPI.as_view(), name='snippet-delete'),

    path('tags/', TagListAPIView.as_view(), name='tag-list'),
    path('tags/<int:pk>/', TagDetailAPIView.as_view(), name='tag-detail'),
]
