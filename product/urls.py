from django.urls import path

from .views import GameBaseDataView,GameCartListView

app_name='product'

urlpatterns = [
    path("game/<int:pk>/",GameBaseDataView.as_view(), name="game_base_data"),
    path("games/",GameCartListView.as_view(), name="game_cart_list")
]
