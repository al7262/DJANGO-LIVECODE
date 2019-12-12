from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name="index"),
    path('item/<int:item_id>', views.detail, name="detail"),
    path('item/new', views.new, name="new"),
    path('item/posted', views.posted, name='posted')
]
