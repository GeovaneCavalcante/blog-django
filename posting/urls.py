from django.urls import path
from .views import index, new, detail

urlpatterns = [
    path('', index),
    path('new', new),
    path('postings/<int:id>/', detail, name='postings'),
]
