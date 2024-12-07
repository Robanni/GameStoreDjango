from django.urls import path

from .views import GameBaseDataView,GameCardListView

app_name='product'

urlpatterns = [
    path("game/<int:pk>/",GameBaseDataView.as_view(), name="game_base_data"),
    path("games/",GameCardListView.as_view(), name="game_cart_list")
]
