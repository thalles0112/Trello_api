from django.urls import path

from . import views

urlpatterns = [
    path("boards", views.boards, name='boards'), 
    path("board/<str:room_name>/", views.board, name="board"),
]