from django.urls import path
from .views import SnippetCreateAPI, SnippetOverviewAPI

urlpatterns = [
    path('snippets/', SnippetOverviewAPI.as_view(), name='snippet-overview'),
    path('snippets/create/', SnippetCreateAPI.as_view(), name='snippet-create'),

]
