
from django.urls import path

from game2048.views.Index_View_game2048 import *





app_name="game2048"

urlpatterns=[



    path('game2048/', Index_View_Game2048.as_view(), name="index"),


]