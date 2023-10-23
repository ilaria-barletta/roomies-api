from django.urls import path
from grocery_list import views

urlpatterns = [
    path("grocerylists/", views.GroceryListList.as_view()),
    path("grocerylists/<int:pk>/", views.GroceryListDetail.as_view()),
    path("groceryitems/", views.GroceryItemList.as_view()),
    path("groceryitems/<int:pk>/", views.GroceryItemDetail.as_view()),
    path("grocerylistcomments/", views.GroceryListCommentList.as_view()),
    path("grocerylistcomments/<int:pk>/", views.GroceryListCommentDetail.as_view()),
]
