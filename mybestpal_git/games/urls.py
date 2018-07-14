
from django.urls import path


from gametictactoe.views.gametictactoe import *



app_name="gametictactoe"

urlpatterns=[

    path('game_tictactoe/', Index_View_GameTicTacToe.as_view(), name="index"),


]