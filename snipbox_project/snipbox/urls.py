from django.urls import path
from .views import SnippetCreateAPI, SnippetOverviewAPI, SnippetDetailAPI
from .views import TagListAPIView


urlpatterns = [
    path('snippets/', SnippetOverviewAPI.as_view(), name='snippet-overview'),
    path('snippets/create/', SnippetCreateAPI.as_view(), name='snippet-create'),
    path('snippets/<int:pk>/', SnippetDetailAPI.as_view(), name='snippet-detail'),


    path('tags/', TagListAPIView.as_view(), name='tag-list'),
]
