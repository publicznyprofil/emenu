from django.conf.urls import url

from .views import (
    MainPageView,
    MenuListAPIView,
    DishListAPIView,
)

urlpatterns = [
    url('^$', MainPageView.as_view(), name='menu_list'),
    url('^api/menus/$', MenuListAPIView.as_view(), name='api_menu_list'),
    url('^api/dishes/$', DishListAPIView.as_view(), name='api_dish_list'),
]
