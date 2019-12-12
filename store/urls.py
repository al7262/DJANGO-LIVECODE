from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name="index"),
    path('barang/<int:item_id>', views.detail, name="detail")
]
