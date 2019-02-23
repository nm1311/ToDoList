from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/add_item', views.add_item, name='add_item'),
    path('/item_complete/<int:pk>', views.item_complete, name='item_complete'),
    path('/delete_item/<int:pk>', views.delete_item, name='delete_item'),
    path('/delete_completed', views.delete_completed, name='delete_completed'),
    path('/reset', views.reset, name='reset'),
    path('/mark_impt/<int:pk>', views.mark_impt, name='mark_impt'),
    path('/show_impt', views.show_impt, name='show_impt'),
    path('/remove_impt/<int:pk>', views.remove_impt, name='remove_impt'),

]
