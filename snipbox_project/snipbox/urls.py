from django.urls import path
from .views import SnippetCreateAPI, SnippetOverviewAPI
from .views import TagListAPIView


urlpatterns = [
    path('snippets/', SnippetOverviewAPI.as_view(), name='snippet-overview'),
    path('snippets/create/', SnippetCreateAPI.as_view(), name='snippet-create'),

    path('tags/', TagListAPIView.as_view(), name='tag-list'),
]
