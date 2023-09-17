from django.urls import path
from grocery_list import views

urlpatterns = [
    path("grocerylists/", views.GroceryListList.as_view()),
]
