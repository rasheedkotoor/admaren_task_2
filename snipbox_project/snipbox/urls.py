from django.urls import path
from .views import SnippetCreateAPI

urlpatterns = [
    path('snippets/create/', SnippetCreateAPI.as_view(), name='snippet-create'),

]
