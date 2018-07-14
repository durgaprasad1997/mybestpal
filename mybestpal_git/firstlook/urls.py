
from django.urls import path
from firstlook.views.index_view import *
from firstlook.views.second_view import *

from mytask.views.my_task import *

app_name="firstlook"

urlpatterns=[

    path('', Index_View.as_view(), name="index"),
    path('index/', Index_View.as_view(), name="index"),

    path('menu_index/', Second_View.as_view(), name="menu_index"),



]