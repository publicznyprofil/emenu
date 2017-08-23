from django.db.models import Count
from django.views.generic import TemplateView
from rest_framework.generics import ListAPIView

from .models import (
    Menu,
    Dish,
)
from .paginations import MenuPagination
from .serializers import (
    MenuListSerializer,
    DistListSerializer,
)


class MainPageView(TemplateView):
    template_name = 'menu/main_page.html'


class MenuListAPIView(ListAPIView):
    queryset = Menu.objects.annotate(dish_number=Count('dishes')).filter(dish_number__gt=0)
    serializer_class = MenuListSerializer
    pagination_class = MenuPagination
    sortable_columns = ['name', 'dish_number']

    def get_queryset(self):
        qs = super().get_queryset()
        sort = self.get_sort()
        if sort:
            return qs.order_by(sort)
        return qs

    def get_sort(self):
        sort = self.request.GET.get('sort')
        if sort in self.sortable_columns:
            if self.request.GET.get('dir') == 'desc':
                sort = '-' + sort
            return sort
        return None


class DishListAPIView(ListAPIView):
    serializer_class = DistListSerializer

    def get_queryset(self):
        return Dish.objects.filter(menu__id=self.request.GET.get('id'))
