from django.urls import path
from .views import upload_vendas, ranking_vendas


urlpatterns = [
    path('upload/', upload_vendas, name='upload_vendas'),
    path('ranking/', ranking_vendas, name='ranking'),
]
