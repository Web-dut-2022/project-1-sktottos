
from django.urls import path
from django import template
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:entry_name>/', views.AllPages, name="AllPages"),
    path('Error', views.Error),
    path("search_item/", views.search_item),
    path("create_new_page/",views.create_new_page,name="create_new_page"),
    path("new_entry/",views.new_entry,name="new_entry")
]
