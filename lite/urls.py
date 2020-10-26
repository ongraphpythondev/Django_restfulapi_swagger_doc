from django.urls import path

from lite.views import *

app_name = 'lite'

urlpatterns = [
    path('author_cls/<int:pk>/', AuthorView.as_view(), name='author'),
    path('author_cls/', AuthorView.as_view(), name='author_create'),
    path('reader_cls/', ReaderView.as_view(), name='reader'),
]