from django.urls import path
from moves.views import MovieView

urlpatterns = [
    path('', MovieView.as_view()), ]
