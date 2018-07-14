
from django.urls import path


from games.views.Index_View_Game import *



app_name="games"

urlpatterns=[

    path('gamemenu/', Index_View_Game.as_view(), name="index"),





]